from django.shortcuts import redirect, render

from accounts.forms import UserForm
from accounts.models import User

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = User.CUSTOMER
            user.save()
            return redirect('register_user')

    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register_user.html', context)
