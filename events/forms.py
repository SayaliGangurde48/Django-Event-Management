from django import forms
from .models import EventUpload


class EventUploadForm(forms.ModelForm):

    class Meta:
        model = EventUpload
        fields = ['event_type', 'event_date', 'csv_file']

        widgets = {
            'event_type': forms.Select(attrs={
                'class': 'form-control'
            }),

            'event_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'csv_file': forms.ClearableFileInput(attrs={
                'accept': '.csv',
                'class': 'form-control'
            }),
        }

    def clean_csv_file(self):

        file = self.cleaned_data.get('csv_file')

        if file:

            if not file.name.lower().endswith('.csv'):
                raise forms.ValidationError(
                    "Only CSV files are allowed."
                )

            if file.size == 0:
                raise forms.ValidationError(
                    "The uploaded file is empty."
                )

            if file.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "File size must not exceed 5 MB."
                )

        return file