from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name


class Quality(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    parameter_name = models.CharField(max_length=100)
    error_description = models.CharField(max_length=500)
    weightage = models.BigIntegerField()

    def __str__(self):
        return self.template_name