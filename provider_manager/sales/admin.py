from django.contrib import admin
from django.shortcuts import redirect
from django.db.models import Sum

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
    form = OrderDetailSaleForm

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("createdAt","number","client","total","is_paid",'utility')
    form = OrderForm
    # actions = [order_selected]
    
    def utility(self, obj):
        if obj.is_paid:
            total = Utility.objects.filter(orderdetail__order=obj.id).aggregate(Sum('value'))
            return total['value__sum']
        return 0
    
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
    
