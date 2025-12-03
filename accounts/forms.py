from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class LoginForm(AuthenticationForm):
    """Authentication form with Bootstrap styling."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{css_classes} form-control'.strip()
            field.widget.attrs.setdefault('placeholder', field.label)


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'role')

    email = forms.EmailField(required=True)
