from django.db import models

class Students(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=20)
    dob = models.DateField()
    age = models.IntegerField()

