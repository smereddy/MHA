from django.contrib import admin
from django.urls import path, include
from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from work_order.models import WorkOrder
from work_order.views import CreateWorkOrder, UpdateWorkOrder, DeleteWorkOrder, WorkOrderDetail, CreateWorkOrderItems, \
    UpdateWorkOrderItems, DeleteWorkOrderItems

urlpatterns = [
    path('create/', CreateWorkOrder.as_view(), name='order_create'),
    path('view/<int:pk>/', WorkOrderDetail.as_view(), name='order_detail'),
    path('edit/<int:pk>/', UpdateWorkOrder.as_view(), name='order_update'),
    path('delete/<int:pk>/', DeleteWorkOrder.as_view(), name='order_delete'),
    path('item/<int:work_order_id>/create/', CreateWorkOrderItems.as_view(), name='item_create'),
    path('item/edit/<int:pk>/', UpdateWorkOrderItems.as_view(), name='item_update'),
    path('item/delete/<int:pk>/', DeleteWorkOrderItems.as_view(), name='item_delete'),
]