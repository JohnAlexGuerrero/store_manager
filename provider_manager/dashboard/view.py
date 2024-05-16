from typing import Any
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.query import QuerySet

from django.views.generic import TemplateView, ListView

from datetime import datetime
from django.db.models import Sum, Count
from decimal import Decimal

from sales.models import Order
from provider.models import Bill, Company
from payments.models import Provider

class HomeView(TemplateView):
  paginate_by = 8
  template_name = 'dashboard/index.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context =  super().get_context_data(**kwargs)
    orders = Order.objects.all().order_by('-createdAt')
    
    context['sales'] = self.orders_per_paginate(orders, paginate=self.paginate_by)
    context['orders'] = orders
    context['sales_per_month'] = self.orders_total_month(orders=orders)

    return context
  
  def orders_per_paginate(self, orders, paginate):
    paginator = Paginator(orders, paginate)
    page = self.request.GET.get('page')
    
    try:
      page_obj = paginator.page(page)
    except PageNotAnInteger:
      page_obj = paginator.page(1)
    except EmptyPage:
      page_obj = paginator.page(paginator.num_pages)

    return page_obj
  
  def orders_total_month(self, orders) -> dict[str: Any]:
    sales_total_by_month = []
    
    for month in [1,2,3,4,5,6,7,8,9,10,11,12]:
      totals = [x.total for x in orders if int(x.createdAt.strftime("%m")) == month]
      sales_total_by_month.insert((month - 1), int(sum(totals)))
      
    return sales_total_by_month
#https://dribbble.com/shots/16203931-Invo-Invoicing-Web-Application

class SearchDateView(ListView):
  model = Order
  template_name = 'dashboard/index.html'
  
  def get_queryset(self):
    query = self.request.GET.get('q')
    object_list = Order.objects.filter(
      createdAt__icontains=query
    )

    return object_list
  
  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context['sales'] = self.get_queryset()
    print(context)
    return context
  
class ProviderViewList(ListView):
  model = Company
  template_name = 'dashboard/bill.html'

  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    companies = Company.objects.filter(bill__is_paid=0).order_by('name').distinct()

    context['companies'] = companies
    context['balance'] = self.company_balance(companies)
    context['total'] = self.total_balance(companies)
    return context
  
  def total_balance(self, companies):
    total = 0
    
    for item in self.company_balance(companies):
      total += item['balance']
    return f'{total:,.2f}'
  
  def company_balance(self, companies):
    res = []
    
    for item in companies:
      query_bills = Bill.objects.filter(company_id=item.id, is_paid=0)
      balance = 0
      for bill in query_bills:
        pays = Provider.objects.filter(bill_id=bill.id)
        total = 0
        
        if pays:
          total = pays.aggregate(Sum('value'))['value__sum']
          
        balance_bill = bill.total - total
        balance += balance_bill
        
      res.append(
        {
          "id": item.id,
          "name": item.name,
          "balance": balance,
          "count": query_bills.count() if query_bills else 0
        }
      )
      
    return res
  