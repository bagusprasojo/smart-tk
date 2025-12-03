from django import forms

from accounts.models import User
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'name',
            'class_name',
            'parents_name',
            'parents_phone',
            'guardian',
            'photo',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guardian'].queryset = User.objects.filter(role=User.Roles.PARENT)
        self.fields['guardian'].required = False
