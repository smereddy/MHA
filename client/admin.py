from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
   model = Client
   list_display = ['client_name', 'mobile_phone', 'work_phone', 'comments']
   list_filter = ['client_name', 'mobile_phone', 'work_phone', 'comments']
   fieldset = (
         ('Resident Information', {
            'fields': ('client_name', 'mobile_phone', 'work_phone', 'comments')
        })
   )
   add_fieldset = (
         ('Resident Information', {
            'fields': ('property_name', 'street_address', 'city', 'state', 'zipcode', 'age_in_years')
        })
   )

admin.site.register(Client, ClientAdmin)
