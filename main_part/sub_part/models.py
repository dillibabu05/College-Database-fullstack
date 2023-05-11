from django.db import models

# Create your models here.
class register_table(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    email_id=models.EmailField(max_length=30)
    profile_picture=models.ImageField(upload_to='documents')
    
class admission_table(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    email=models.EmailField()
    course=models.CharField(max_length=100)

class contact_table(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField()
