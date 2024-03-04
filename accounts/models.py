from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, user_name, email, password):
        # validations
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not user_name:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        
        # create user
        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, first_name, last_name, user_name, email, password):
        # create user
        user = self.create_user(
            email = self.normalize_email(email),
            user_name = user_name,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        # set user as admin
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    

# Custom User Model
class User(AbstractBaseUser):
    RESTURANT = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (RESTURANT, 'Resturant'),
        (CUSTOMER, 'Customer')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    password = models.CharField(max_length=100)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # Django required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures/', blank=True, null=True)
    cover_picture = models.ImageField(upload_to='users/cover_pictures/', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.user_name
