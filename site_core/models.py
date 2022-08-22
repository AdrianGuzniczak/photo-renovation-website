from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Photo(models.Model):
    renovation = models.BooleanField(default=False)
    coloring = models.BooleanField(default=False)
    description = models.CharField(max_length=150, default=None)
    photo = models.ImageField(upload_to='media/photos')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, editable=False)
    print('<<<<<<<<<<<<<<<<<<<<  {}'.format(user))
    

    def __str__(self):
        return f"Photo submitted for restoration."
