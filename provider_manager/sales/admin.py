from django.contrib import admin
from sales.models import OrderDetailSale, Order, Client
from sales.forms import OrderForm, ClientForm, OrderDetailSaleForm

# Register your models here.
@admin.register(OrderDetailSale)
class OrderDetailSaleAdmin(admin.ModelAdmin):
    form = OrderDetailSaleForm

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("createdAt","number","client","total","is_paid")
    form = OrderForm

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
