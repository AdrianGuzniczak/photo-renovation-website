from curses.textpad import Textbox
from email import message
from tkinter import Widget
from django import forms
# from django.forms import ModelForm
from .models import Contact
from django.core.mail import send_mail
from datetime import datetime

    
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


    def send_email(self):

        print(self.cleaned_data['email'])
        print(self.cleaned_data['subject'])
        print(self.cleaned_data['message'])

        now = datetime.now()
        date_and_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

        auto_message = 'On {} at {} we received your message with the following content: \n\n{}\n{} \n\n We will try to answer it soon. Please do not reply to this message. \n\n The photo renovation website team.'.format(date_and_time_string.split()[0], date_and_time_string.split()[1], self.cleaned_data['subject'], self.cleaned_data['message'])

        print(auto_message)
         
        send_mail('Photo renovation website - contact', message = auto_message, from_email = 'test.photo.renovation.website@gmail.com', recipient_list = [self.cleaned_data['email']], fail_silently=False)
