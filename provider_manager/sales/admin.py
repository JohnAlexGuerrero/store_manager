from django.contrib import admin
from django.shortcuts import redirect
from django.db.models import Sum
from decimal import Decimal

from sales.models import OrderDetailSale, Order, Client
from sales.forms import ClientForm, OrderForm, OrderDetailSaleForm
from payments.models import SalesBill, Utility

# Register your models here.
def select_one_item(modeladmin,request, queryset):
    if queryset.count() == 1:
        item = queryset.first()
        if item:
            return item
    modeladmin.message_user(request, "Por favor selecciona una sola cuenta")
    



@admin.register(OrderDetailSale)
class OrderDetailSaleAdmin(admin.ModelAdmin):
    list_display = ['product','amount','price','total','revenue','utility']
    
    def total(self, obj):
        return obj.amount * obj.price
    
    def revenue(self, obj):
        return (obj.price - obj.product.cost_with_tax)* obj.amount
    
    def utility(self, obj):
        util = round((obj.price - obj.product.cost_with_tax) / obj.price, 2)
        return f'{util * 100} %'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("createdAt","number","client","total",'utility','revenue',"is_paid")
    form = OrderForm
    # actions = [order_selected]
    
    def revenue(self, obj):
        if obj.is_paid:
            total = Utility.objects.filter(orderdetail__order=obj.id).aggregate(Sum('value'))
            return f'$ {total['value__sum']:,.2f}'
        return 0
    
    def utility(self, obj):
        sum_utility = 0
        num_utility = 0
        
        if obj.is_paid:
            query = OrderDetailSale.objects.filter(order=obj.id)
            num_utility = len(query)
            for item in query:
                sum_utility += ((item.total - (item.product.cost_with_tax * item.amount)) / item.total) * 100
        
            return f'{round(sum_utility / num_utility,2)} %'
        return '0 %'
    
    def view_sale_order(modeladmin, request, queryset):
        item = select_one_item(modeladmin, request, queryset)
        if item:
            return redirect('invoice-detail', pk=item.id)
    
    def pay_sale_order(modeladmin, request, queryset):
        item = select_one_item(modeladmin, request, queryset)
        if item.is_paid != True:
            item.is_paid = True
            pay_sale = SalesBill(order=item, total=item.total, way_to_pay='efectivo', createdAt=item.createdAt)
            pay_sale.save()
            item.save()
        modeladmin.message_user(request, 'La factura esta cancelada.')
            
    admin.site.add_action(view_sale_order, 'Ver')
    admin.site.add_action(pay_sale_order, 'pagar')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    
