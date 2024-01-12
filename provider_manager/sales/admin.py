from django.contrib import admin
from django.shortcuts import redirect
from sales.models import OrderDetailSale, Order, Client
from sales.forms import OrderForm, ClientForm, OrderDetailSaleForm

# Register your models here.
def order_selected(modeladmin, request, queryset):
    if queryset.count() == 1:
        item = queryset.first()
        print(item)
        return redirect('invoice-detail', pk=item.id)

order_selected.short_description = "show invoice"

@admin.register(OrderDetailSale)
class OrderDetailSaleAdmin(admin.ModelAdmin):
    form = OrderDetailSaleForm

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("createdAt","number","client","total","is_paid")
    form = OrderForm
    actions = [order_selected]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
