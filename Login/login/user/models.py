from django.db import models

# Create your models here.
class Login(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    
class Signup(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name