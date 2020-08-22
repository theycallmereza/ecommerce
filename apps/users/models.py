from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import MobileValidator


# Create your models here.
class User(AbstractUser):
    """Customize default Django user model"""
    # mobile_number = models.CharField(_("Mobile Number"), max_length=11, unique=True, validators=[MobileValidator])
    pass