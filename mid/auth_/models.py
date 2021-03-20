from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


# class UserProfileManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, username, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not username:
#             raise ValueError('The given username must be set')
#         username = self.normalize_email(username)
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(username, password, **extra_fields)
#
#     def create_superuser(self, username, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)


class UserProfile(AbstractUser):
    class Roles(models.TextChoices):
        SUPER_ADMIN = 'SuperAdmin', _('SuperAdmin')
        GUEST = 'Guest', _('Guest')
    role = models.CharField(max_length=20, choices=Roles.choices,
                            default=Roles.GUEST)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class UserProfile(AbstractBaseUser):
#     class Roles(models.TextChoices):
#         SUPER_ADMIN = 'SuperAdmin', _('SuperAdmin')
#         GUEST = 'Guest', _('Guest')
#     username = models.CharField(_('username'), unique=True, max_length=20)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     is_active = models.BooleanField(_('active'), default=True)
#     is_staff = models.BooleanField(_('is_staff'), default=True)
#     extra_info = models.TextField(max_length=200, default='No extra info')
#     role = models.CharField(max_length=20, choices=Roles.choices,
#                             default=Roles.GUEST)
#
#     objects = UserProfileManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'
