from typing import Any
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal

from sales.models import Order

class HomeView(TemplateView):
  paginate_by = 8
  template_name = 'dashboard/index.html'
  
  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context =  super().get_context_data(**kwargs)
    orders = Order.objects.all().order_by('createdAt')
    
    context['sales'] = self.orders_per_paginate(orders, paginate=self.paginate_by)
    context['sales_per_month'] = self.orders_total_month(orders=orders)
    print(context)

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