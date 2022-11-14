from django.db import models

# Create your models here.

class User (models.Model):
    emp_name =  models.CharField(max_length=70)
    email =  models.EmailField(max_length=100)
    work =  models.CharField(max_length=100)