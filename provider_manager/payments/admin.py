from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Sum
from django.http.request import HttpRequest
from payments.models import Provider, SalesBill
from provider.models import Bill
from sales.models import Utility
from payments.forms import ProviderForm


# Register your models here.
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['company_display','bill','createdAt','value',"balance"]
    list_filter = (
        ('createdAt',)
    )
    search_fields = ("bill__number",)
    
    form = ProviderForm
    
    def balance(self, obj):
        pays = Bill.objects.filter(number=obj.bill) #Provider.objects.filter(bill=obj.bill)
        print(pays)
        return 0
    
    def get_bill_pending(self, obj):
        return []
    
    # search_fields = ['bill',]

    def company_display(self, obj):
        return obj.bill.company

    
@admin.register(SalesBill)
class SalesBillAdmin(admin.ModelAdmin):
    list_display = ("createdAt","order","total","utility","way_to_pay")

    def utility(self, obj):
        res = Utility.objects.filter(orderdetail__order_id=obj.order).aggregate(Sum('value'))
        return res 
    
