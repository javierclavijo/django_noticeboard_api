from django import forms
from .models import Notice
from django.utils import timezone


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'body', 'exp_date']
        widgets = {
            'exp_date': forms.DateInput(attrs={'type': 'date'}),
            'body': forms.Textarea,
        }

    def clean(self):
        cleaned_data = super().clean()
        exp_date = cleaned_data.get("exp_date")

        if exp_date <= timezone.now():
            msg = "Expiration date must be in the future."
            self.add_error('exp_date', msg)
