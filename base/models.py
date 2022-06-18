from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
import uuid


# Create your models here.
class User(AbstractUser):
   email = models.EmailField(unique=True)
   bio = models.TextField(null=True)
   neighboorhood = models.CharField(max_length=100, null=True)
   image = CloudinaryField('image', null=True, blank=True, default='image/upload/v1654285390/hz7a08c74kynhnx24lwd.png')
   contact = models.CharField(max_length=100 ,blank=True, null=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']