from django.db import models

# Create your models here.

class SignupTB(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    