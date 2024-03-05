from django.shortcuts import redirect, render
from django.contrib import messages

from accounts.forms import UserForm
from accounts.models import User

# Create your views here.
def register_user(request):
    # GET request
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register_user.html', context)
    
    # POST request
    if request.method == 'POST':
        form = UserForm(request.POST)

        # valid form data
        if form.is_valid():
            # User creation using create_user() from UserManager
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user_name = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                email=email,
                password=password
            )
            # Assign role and save user
            user.role = User.CUSTOMER
            user.save()
            # Show successful registration message
            messages.success(request, 'Your account is registered successfully')
            # go back to Registration page after successful form submission
            return redirect('register_user')
        
        # invalid form data
        context = {
            'form': form
        }
        return render(request, 'accounts/register_user.html', context)


# Vendor registration
def register_vendor(request):
    return render(request, 'accounts/register_vendor.html')