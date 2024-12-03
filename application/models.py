from django.db import models

# Create your models here.

class Customer (models.Model):
    name = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    # Constructor to return one of the values
    def __str__(self):
        return self.name
