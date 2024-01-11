from django.shortcuts import render
from payments.models import Provider
from django.views.generic import DetailView
from provider.models import Bill
from payments.forms import ProviderForm

# Create your views here.

class ProviderDetailView(DetailView):
    model = Provider
    template_name = "payments/provider.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bill = Bill.objects.get(id=self.kwargs['pk'])
        if bill:
            context["bill"] = bill
            context['pays'] = Provider.objects.filter(bill_id=bill.id)
        context['form'] = ProviderForm
        print(context)
        return context
    