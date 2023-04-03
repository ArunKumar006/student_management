from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from django.db import models



class CustomUser(AbstractBaseUser):
    email = models.EmailField(_("email address"), unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
