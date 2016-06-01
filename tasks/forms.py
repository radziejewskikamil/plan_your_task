from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    date = forms.CharField(widget=forms.DateInput(attrs={"class": "form-control form_input", "readonly": ""}))
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form_input"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form_input"}), required=False)

    class Meta:
        model = Tasks
        fields = ('date', 'title', 'description')
