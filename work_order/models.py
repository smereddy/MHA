from django.db import models
from property.models import Apartment
from user.models import AppUser


# Create your models here.
class WorkOrder(models.Model):

    severity_choices = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('EMERGENCY', 'Emergency')
    ]
    status_choices = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed')
    ]
    work_order_name = models.CharField(max_length=30, blank=False, default='', verbose_name = 'Title')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, verbose_name = 'Apartment Number')
    description = models.CharField(max_length=200, blank=False, default='')
    skillset_required = models.CharField(max_length=200, blank=False, default='', verbose_name = 'Skillset Required')
    severity_level = models.CharField(max_length=9, blank=False, default='Low', choices=severity_choices, verbose_name = 'Severity')
    current_status = models.CharField(max_length=25, blank=False, default='Open', choices=status_choices, verbose_name = 'Current Status')
    desired_completion_date = models.DateTimeField(blank=True, null=True, verbose_name = 'Desired Completion Date')
    actual_completion_date = models.DateTimeField(blank=True, null=True, verbose_name = 'Actual Completion Date')
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, default='0.0', verbose_name = 'Estimated Cost')
    actual_cost = models.DecimalField(max_digits=8, decimal_places=2, default='0.0', verbose_name = 'Actual Cost')
    work_order_date = models.DateTimeField(blank=True, null=True, verbose_name = 'Submitted Date')
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, verbose_name = 'Work Order Submitted By')

    def __str__(self):
        return self.work_order_name

class WorkOrderItem(models.Model):
    item_name = models.CharField(max_length=30, blank=False, verbose_name = 'Item Name')
    item_cost = models.DecimalField(max_digits=8, decimal_places=2, default='0.0', verbose_name = 'Cost')
    item_quantity = models.IntegerField(default=1, blank=False, verbose_name = 'Quantity')
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, verbose_name = 'Associated Work Order')

    def __str__(self):
        return self.item_name