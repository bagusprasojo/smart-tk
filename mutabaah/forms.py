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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            css_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{css_classes} form-control'.strip()
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs.setdefault('rows', 3)
