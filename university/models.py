from distutils.command.upload import upload
from email.policy import default
from turtle import width
from django.db import models

# Create your models here.
class University(models.Model):
    city = models.CharField(max_length= 30)
    name = models.CharField(max_length= 30)
    acronym = models.CharField(max_length= 10)
    logo = models.ImageField(upload_to = 'imags/', blank=True , null=True, default = 'imags/images.png' )
    type = models.CharField(max_length = 10)
    overview = models.TextField()
    founded = models.IntegerField()
    total_student = models.IntegerField()
    international_students = models.IntegerField()
    site = models.CharField(max_length= 100)
    acceptance_rate = models.IntegerField()
