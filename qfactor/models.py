from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Element(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="files/")

        

    def __str__(self):
        return self.name

    def clean(self):
        if Element.objects.filter(name=self.name).count() > 0:
            raise ValidataionError("Duplicates exist. Please try a different name.")
    
    