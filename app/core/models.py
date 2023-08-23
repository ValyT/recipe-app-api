""""
Database models
"""
from django.db import models
from django.contrib.auth.modles import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, email, password=None, **extra_field):
        """Creates, save, return new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self_db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    object=UserManager()

    USERNAME_FIELD='email'
