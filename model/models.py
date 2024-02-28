from django.db import models

class Students(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)
    dob = models.DateField()
    age = models.IntegerField()

class Meta:
 db_table = "students"

class Teachers(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)

    def __str__(self):
        return self.firstname

class parents(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    emailaddress = models.EmailField(max_length=30)


    def __str__(self):
        return self.firstname

class post(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=220)
    author = models.CharField(max_length=30)
    CreatedAt = models.TimeField()

    def __str__(self):
        return self.title


