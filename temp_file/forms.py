from django import forms
from .models import UploadFile


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ('name', 'text', 'upload', 'finish_date')
        widgets = {'finish_date': forms.DateTimeInput()}