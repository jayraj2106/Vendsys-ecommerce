from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    address = models.CharField(max_length=255, blank=False)
    phone_no = models.CharField(max_length=15, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    

    def __str__(self):
        return self.username
