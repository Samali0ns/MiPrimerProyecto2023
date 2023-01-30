
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profileuser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
    bio=models.TextField(default='ingrese su bio',null=True, blank=True)
