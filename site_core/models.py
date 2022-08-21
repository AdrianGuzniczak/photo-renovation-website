from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

# Create your models here.
class Photo(models.Model):
    renovation = models.BooleanField(default=False)
    coloring = models.BooleanField(default=False)
    description = models.CharField(max_length=150, default=None)
    # photo = models.ImageField(storage=fs)

    def __str__(self):
        return f"Photo submitted for restoration."
