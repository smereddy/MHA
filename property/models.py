from django.db import models
from client.models import Client


class Property(models.Model):
    property_name = models.CharField(max_length=30, default='', blank=False, verbose_name = 'Property Name')
    street_address = models.CharField(max_length=40, default='', blank=False, verbose_name = 'Street Address')
    city = models.CharField(max_length=20, blank=False, default='')
    state = models.CharField(max_length=2, blank=False, default='NE')
    zipcode = models.CharField(max_length=9, blank=False, default='', verbose_name = 'Zip Code')
    age_in_years = models.CharField(max_length=2, default = '', blank=True, null=True, verbose_name = 'Age (In Years)')

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.property_name


class Apartment(models.Model):
    apt_num = models.CharField(max_length=5, default='', blank=False, verbose_name = 'Apartment Number')
    size_in_sqft = models.IntegerField(default=0, blank=False, verbose_name = 'Size (sqft)')
    number_of_bedrooms = models.IntegerField(default=0, blank=False, verbose_name = 'Number of Bedrooms')
    description = models.CharField(max_length=300, default='', blank=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name = 'Property')
    client = models.ForeignKey(Client, default=1, on_delete=models.SET_DEFAULT, verbose_name = 'Resident')

    def __str__(self):
        return self.apt_num
