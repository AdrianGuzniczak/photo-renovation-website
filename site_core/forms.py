from curses.textpad import Textbox
from tkinter import Widget
from django import forms
# from django.forms import ModelForm
from .models import Contact

    
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    # widgets = {
    #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
    #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
    #     'message': forms.TextInput(attrs={'class': 'form-control'})
    # }

