from django.db import models

class Company(models.Model):

    name=models.CharField(max_length=100)
    direccion=models.URLField(max_length=100)
    fundation=models.DateField()
    imagen=models.ImageField(upload_to='Company_Image')

    def __str__(self) :
        return self.name

# Create your models here.
