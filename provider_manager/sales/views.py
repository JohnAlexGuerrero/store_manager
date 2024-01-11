from django.shortcuts import render
from sales.models import Order, Client, OrderDetailSale
from inventory.models import Product
from django.views.generic import TemplateView
from django.views.generic import CreateView
from datetime import datetime
from sales.forms import OrderDetailSaleForm

# Create your views here.
class OrderView(TemplateView):
    template_name = "sales/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.object_order()
        context["order"] = order
        context['items'] = Product.objects.all()
        context["form"] = OrderDetailSaleForm
        print(context)
        return context
    
    def object_order(self):
        obj_order = Order(
            number=f'{Order.objects.all().count() + 4090}',
            createdAt=datetime.now(),
            total=0.0,
            client=Client.objects.first(),
            user_id=1
        )
        return obj_order

class OrderDetailSaleCreateView(CreateView):
    model = OrderDetailSale
    form_class = OrderDetailSaleForm
    print(form_class)
    template_name = "sales/order_detail_sale.html"
