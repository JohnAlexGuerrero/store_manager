from django.shortcuts import render

from sales.models import Order, Client

from django.views.generic import CreateView
from django.views.generic import TemplateView

# Create your views here.
class InvoiceCreateView(TemplateView):
    template_name = "invoicing/invoice.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.all()
        return context
    
