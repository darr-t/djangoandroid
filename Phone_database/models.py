from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    sports = models.CharField(max_length=100, null=True, blank=True)
   
    class Meta:
        db_table = 'students'
# python manage.py makemigrations
# python manage.py migrate
# pip install django_rest_framework........install api needed
