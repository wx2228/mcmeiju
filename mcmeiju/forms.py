from django import forms
from django.core import validators
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    