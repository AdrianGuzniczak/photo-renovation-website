from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    '''Use the 'Photo reconstruction' tab to create an instance of this class.
    These instances are displayed in the "my photos" tab.
    This class is used by PhotoCreateView, PhotoDeleteView and PhotoListView in the vievs.py file'''

    description = models.CharField(max_length=150, default=None)
    photo = models.ImageField(upload_to='media/photos')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.description}"

class Contact(models.Model):

    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
