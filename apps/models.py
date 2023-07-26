from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

#
class Register(AbstractUser):
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    skype = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField()
    facebook = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)
    dribble = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    pinterest = models.CharField(max_length=255, blank=True, null=True)

    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.seiu1000.org%2Fpost%2Fimage-dimensions&psig=AOvVaw0tFRjj-J4ehUZF32uIXfpR&ust=1690435824553000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJDroqjSq4ADFQAAAAAdAAAAABAE'
