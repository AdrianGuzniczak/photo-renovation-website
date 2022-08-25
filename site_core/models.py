from contextlib import nullcontext
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse

# Create your models here.
class Photo(models.Model):

    def get_user_id(request):
        current_user = request.user
        return current_user.id

    renovation = models.BooleanField(default=False)
    coloring = models.BooleanField(default=False)
    description = models.CharField(max_length=150, default=None)
    photo = models.ImageField(upload_to='media/photos')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.description}"

class Contact(models.Model):
    
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
