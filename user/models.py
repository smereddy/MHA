from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    email = models.CharField(max_length=30, blank=False, default='')
    position = models.CharField(max_length=30, blank=False, default=' ')
    skillset = models.CharField(max_length=200, blank=False, default=' ')
    mobile_phone = models.CharField(max_length=10, blank=False, default='', verbose_name = 'Mobile Phone Number')
    work_phone = models.CharField(max_length=10, blank=True, null=True, default='', verbose_name = 'Work Phone Number')

    def __str__(self):
        return self.username
