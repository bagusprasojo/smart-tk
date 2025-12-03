from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'role')

    email = forms.EmailField(required=True)

