from django import forms

from .models import Mutabaah


class MutabaahForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Mutabaah
        fields = (
            'student',
            'date',
            'ibadah',
            'sikap',
            'hafalan',
            'motorik',
            'kemandirian',
            'catatan',
        )
