from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from datetime import datetime

from django.contrib.auth.models import User
from provider.models import Bill, OrderDetail
from payments.models import Provider

from django.views.generic import DetailView
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView

from payments.forms import ProviderForm


# Create your views here.
class ProviderListView(ListView):
    model = Provider
    template_name = "provider/index.html"



class BillDetailView(DetailView):
    model = Bill
    template_name = "bill/detail.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_items"] = OrderDetail.objects.filter(bill=self.kwargs['pk'])
        # pays = Provider.objects.filter(bill_id=context['object'].id)
        # context['pays'] = pays
        print(context)
        return context

class BillPayView(TemplateView):
    template_name = "payments/provider.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.first()
        bill = Bill.objects.get(pk=self.kwargs['pk'])
        ref = f'RCB - {Provider.objects.all().count() + 2931}'

        print(ref)
        data = {'user': user, 'reference':ref, 'bill':bill, 'value':bill.total,'description':'', 'createdAt':datetime.now().strftime('%Y-%m-%d')}
        print(data)
        f = ProviderForm(data)
        context['form'] = f
        return context 

    def post(self,request, *args, **kwargs):
        if request.method == 'POST':
            print(request.POST)
            form = ProviderForm(request.POST)

            if form.is_valid:
                new_object = form.save(commit=False)
                new_object.save()
                print(request.user)
                bill = Bill.objects.get(pk=request.POST.get('bill'))

                return redirect(f"/admin/provider/bill/?company__name={bill.company.name}")

    #     return redirect("bill-pay", pk=self.kwargs['pk'])
    
# class ProviderPayView(TemplateView):
#     model = Bill
#     template_name = 
    
#     def get_object(self, bill_id):
#         return Bill.objects.get(pk=bill_id)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context['form'] = form
#         context['object'] = object

#         print(context)
#         return context
    
#     def get_user_active():
#         return User.objects.first()

#     def post(self, request, *args, **kwargs):
#         user = User.objects.get(username=request.POST.get('user'))
#         bill = Bill.objects.get(number=request.POST.get('bill'))
#         form = ProviderForm()
        
#         if form.is_valid():
            
#             form.user=user.id
#             form.bill=bill.id 
#             form.value=request.POST.get('value')
#             form.reference=request.POST.get('reference')
#             form.createdAt=request.POST.get('createdAt')
#             form.description=request.POST.get('description')
#             form.save()
#             return redirect()   
                 
#         return redirect('bill-pay', pk=bill.id)