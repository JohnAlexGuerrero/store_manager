from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from payments.models import Provider
from payments.forms import ProviderForm

# # Create your views here.
class ProviderCreateView(CreateView):
    model = Provider
    template_name = "payments/provider.html"
    form_class = ProviderForm
    # success_url = reverse_lazy('/admin/provider/bill/')
