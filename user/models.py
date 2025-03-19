from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, null=False, blank=False)
    lastname = models.CharField(max_length=30, null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)

# Create your models here.
