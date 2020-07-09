from django.db import models


# Create your models here.

class Participant(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    groupname = models.CharField(max_length=32)
    email = models.EmailField()
    year = models.IntegerField()

    def __str__(self):
        return self.firstname
