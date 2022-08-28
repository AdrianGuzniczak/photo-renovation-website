from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from .models import Contact


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def send_email(self):
        '''This method allows you to send an e-mail to the user with the information contained in the contact form.'''

        now = datetime.now()
        date_and_time_string = now.strftime("%d/%m/%Y %H:%M:%S")
        auto_message = 'On {} at {} we received your message with the following content: \n\n{}\n{} \n\n We will try to answer it  soon. Please do not reply to this message. \n\n The photo renovation website team.'.format(date_and_time_string.split()[0], date_and_time_string.split()[1], self.cleaned_data['subject'], self.cleaned_data['message'])

        send_mail('Photo renovation website - contact', message = auto_message, from_email = 'test.photo.renovation.website@gmail.com', recipient_list = [self.cleaned_data['email'], ], fail_silently=False)
