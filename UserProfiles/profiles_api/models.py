from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """helps django work with our custom manager."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object"""

        if not email:
            raise ValueError("Users must have email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password=None):
        """creates a super user for the model"""

        user = self.create_user(email=email, name=name, password=password)

        user.is_superuser=True
        user.is_staff=True

        user.save(using=self._db)

        return user





class UserProfile(AbstractBaseUser):
    """Represents user profiles inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Method to get full name of the User."""

        return self.name


    def get_short_name(self):
        """Method to get short name of the User."""

        return self.name


    def __str__(self):
        """Django uses this method to retun the objects in string notation."""

        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
