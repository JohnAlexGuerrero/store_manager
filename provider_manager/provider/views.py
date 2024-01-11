from django.shortcuts import render
from provider.models import Bill
from payments.models import Provider
from payments.forms import ProviderForm
from django.views.generic import DetailView

# Create your views here.
class BillDetailView(DetailView):
    model = Bill
    template_name = "provider/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProviderForm
        pays = Provider.objects.filter(bill_id=context['object'].id)
        context['pays'] = pays
        print(context)
        return context
    
