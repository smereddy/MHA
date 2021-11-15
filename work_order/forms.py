from django import forms
from django.db.models import Model

from work_order.models import WorkOrderItem


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = WorkOrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        work_order_id = kwargs.pop('work_id')
        super(CreateItemForm, self).__init__(*args, **kwargs)
        self.fields['work_order'].initial = work_order_id
