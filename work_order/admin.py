from django.contrib import admin
from .models import WorkOrder, WorkOrderItem


class WorkOrderAdmin(admin.ModelAdmin):
   model = WorkOrder
   list_display = ['work_order_name', 'get_apt_num', 'description', 'skillset_required', 'severity_level', 'current_status', 'desired_completion_date', 'actual_completion_date', 'estimated_cost', 'actual_cost', 'work_order_date', 'get_username']
   list_filter = ['apartment__apt_num', 'skillset_required', 'severity_level', 'current_status', 'estimated_cost', 'actual_cost', 'work_order_date', 'actual_completion_date', 'user__username']
   fieldset = (
         ('Work Order Information', {
            'fields': ('work_order_name', 'apartment_id', 'description', 'skillset_required', 'severity_level', 'current_status', 'desired_completion_date', 'actual_completion_date', 'estimated_cost', 'actual_cost', 'work_order_date', 'user_id')
        })
   )
   add_fieldset = (
         ('Work Order Information', {
            'fields': ('work_order_name', 'apartment_id', 'description', 'skillset_required', 'severity_level', 'current_status', 'desired_completion_date', 'actual_completion_date', 'estimated_cost', 'actual_cost', 'work_order_date', 'user_id')
        })
   )

   def get_apt_num(self, obj):
      return obj.apartment.apt_num
   get_apt_num.admin_order_field = 'apt_num'
   get_apt_num.short_description = 'Apartment Number'

   def get_username(self, obj):
      return obj.user.username
   get_username.admin_order_field = 'username'
   get_username.short_description = 'User'

class WorkOrderItemAdmin(admin.ModelAdmin):
   model = WorkOrderItem
   list_display = ['item_name', 'item_cost', 'item_quantity', 'get_work_order', 'work_order_id']
   list_filter = ['item_name', 'work_order_id']
   fieldset = (
         ('Work Order Item Information', {
            'fields': ('item_name', 'item_cost', 'item_quantity', 'work_order_id')
        })
   )
   add_fieldset = (
         ('Work Order Item Information', {
            'fields': ('item_name', 'item_cost', 'item_quantity', 'work_order_id')
        })
   )

   def get_work_order(self, obj):
      return obj.work_order.work_order_name
   get_work_order.admin_order_field = 'work_order_name'
   get_work_order.short_description = 'Work Order'

admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(WorkOrderItem, WorkOrderItemAdmin)
