from django.contrib import admin
from .models import Property, Apartment

class PropertyAdmin(admin.ModelAdmin):
   model = Property
   list_display = ['property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years']
   list_filter = ['property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years']
   fieldset = (
         ('Property Information', {
            'fields': ('property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years')
        })
   )
   add_fieldset = (
         ('Property Information', {
            'fields': ('property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years')
        })
   )

class ApartmentAdmin(admin.ModelAdmin):
   model = Apartment
   list_display = ['apt_num', 'size_in_sqft', 'number_of_bedrooms', 'description', 'get_property_name', 'get_client_name']
   list_filter = ['number_of_bedrooms', 'property__property_name']
   fieldset = (
         ('Apartment Information', {
            'fields': ('apt_num', 'size_in_sqft', 'number_of_bedrooms', 'description', 'property_id', 'client_id')
        })
   )
   add_fieldset = (
         ('Apartment Information', {
            'fields': ('apt_num', 'size_in_sqft', 'number_of_bedrooms', 'description', 'property_id', 'client_id')
        })
   )

   def get_property_name(self, obj):
      return obj.property.property_name
   get_property_name.admin_order_field = 'property_name'
   get_property_name.short_description = 'Property Name'

   def get_client_name(self, obj):
      return obj.client.client_name
   get_client_name.admin_order_field = 'client_name'
   get_client_name.short_description = 'Resident'


admin.site.register(Property, PropertyAdmin)
admin.site.register(Apartment, ApartmentAdmin)
