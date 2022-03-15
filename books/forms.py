from django import forms
from .models import AddBookModel

class AddBookForm(forms.ModelForm):
    class Meta:
        model = AddBookModel
        fields='__all__'