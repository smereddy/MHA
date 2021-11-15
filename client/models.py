from django.db import models


class Client(models.Model):
    client_name = models.CharField(max_length=30, blank=False, default='', verbose_name='Resident Name')
    mobile_phone = models.CharField(max_length=10, blank=False, default='', verbose_name = 'Mobile Phone Number')
    work_phone = models.CharField(max_length=10, blank=True, null=True, default='', verbose_name = 'Work Phone Number')
    comments = models.CharField(max_length=200, blank=True, null=True, default='')

    def __str__(self):
        return self.client_name
