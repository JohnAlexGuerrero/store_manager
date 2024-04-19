from django.shortcuts import render
from django.db.models import Q

from sales.models import Order, Client, OrderDetailSale
from inventory.models import Product, Category

from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from datetime import datetime
from django.db.models import Sum

from sales.forms import OrderDetailSaleForm

from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
class SearchSalesByMonthView(ListView):
    template_name = "sales/sales_month.html"
    model = Order
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_query = Order.objects.filter(
            Q(createdAt__range=[datetime(2024,3,1), datetime(2024,3,30)])
        )
        return object_query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = self.get_total
        context["categories"] = self.get_total_by_category
        return context
    
    def get_total(self):
        total = 0
        for item in self.get_queryset():
            total = total + item.total
        return f'{total:,.2f}'
    
    def get_total_by_category(self):        
        categories = Category.objects.all().order_by('name')
        for category in categories:
            total = 0
 
            for order in self.get_queryset():
                items = OrderDetailSale.objects.filter(order=order.id, product__category=category.id)
                if items:
                    total_list = [x.total for x in items]
                    total += sum(total_list)
                else:
                    continue
            category.total = f'{total:,.2f}'
        return categories
    

class ShopingCartView(TemplateView):
    template_name = "shopping_cart/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = OrderDetailSaleForm
        return context
    

def pdfReportSales(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Dispositon"] = 'attachment; filename=hello.pdf'
    
    p = canvas.Canvas(response)
    p.setFont("Courier", 28)
    p.drawString(0, 0, "Hola mundo")
    
    p.showPage()
    p.save()
    return response
    


class OrderDetailView(DetailView):
    model = Order
    template_name = "sales/order_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = OrderDetailSale.objects.filter(order=context['object'].id)
        print(context) 
        return context
    


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
