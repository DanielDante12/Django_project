
from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    firstname =models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    dateOfBirth=models.DateField()
    nationality=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    def __str__(self):
        return self.firstname

# Create your models here.
