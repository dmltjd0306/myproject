from django.db import models

# Create your models here.
# Models == database.


class SystemMainModel(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

class DoctorInfo(models.Model):
    callname = models.CharField(max_length=50)
    workplace = models.CharField(max_length=50)
    schedule = models.CharField(max_length=100)
    fee = models.CharField(max_length=30)
    description = models.CharField(max_length=255)


# admin message name. Not working IDK why
def __str__(self):
    return f"{self.firstname} {self.lastname}"
