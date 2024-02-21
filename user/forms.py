from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import UserProfile, Comment, Post, Like, Stories


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
