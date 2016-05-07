from __future__ import unicode_literals

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    wechat = models.TextField()
    email = models.EmailField()
    phone = PhoneNumberField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
