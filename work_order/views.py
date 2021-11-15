import kwargs as kwargs
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from work_order.forms import CreateItemForm
from work_order.models import WorkOrder, WorkOrderItem


class WorkOrderList(LoginRequiredMixin, ListView):
    template_name = "home.html"
    model = WorkOrder

    def get_context_data(self, **kwargs):
        context = super(WorkOrderList, self).get_context_data(**kwargs)
        context["orders"] = WorkOrder.objects.all()
        return context


class WorkOrderDetail(LoginRequiredMixin, DetailView):
    template_name = "work_order/details.html"
    model = WorkOrder

    def get_context_data(self, **kwargs):
        context = super(WorkOrderDetail, self).get_context_data(**kwargs)
        context["items"] = WorkOrderItem.objects.filter(work_order=self.object)
        return context


class CreateWorkOrder(LoginRequiredMixin, CreateView):
    template_name = "work_order/create.html"
    model = WorkOrder
    fields = "__all__"
    success_url = reverse_lazy("home")


class UpdateWorkOrder(LoginRequiredMixin, UpdateView):
    template_name = "work_order/update.html"
    model = WorkOrder
    fields = "__all__"
    success_url = reverse_lazy("home")


class DeleteWorkOrder(LoginRequiredMixin, DeleteView):
    model = WorkOrder
    fields = "__all__"
    success_url = reverse_lazy("home")


class CreateWorkOrderItems(LoginRequiredMixin, CreateView):
    template_name = "work_order/items/create.html"
    model = WorkOrderItem
    form_class = CreateItemForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request, 'work_id': self.kwargs['work_order_id']})
        return kwargs

    def get_success_url(self, **kwargs):
        return reverse_lazy('order_detail', kwargs = {'pk': self.kwargs['work_order_id']})


class UpdateWorkOrderItems(LoginRequiredMixin, UpdateView):
    template_name = "work_order/items/update.html"
    model = WorkOrderItem
    fields = ('item_name','item_cost', 'item_quantity')
    success_url = reverse_lazy("home")

    def get_success_url(self, **kwargs):
        return reverse_lazy('order_detail', kwargs = {'pk': self.object.work_order_id})


class DeleteWorkOrderItems(LoginRequiredMixin, DeleteView):
    model = WorkOrderItem
    fields = "__all__"
    success_url = reverse_lazy("home")
