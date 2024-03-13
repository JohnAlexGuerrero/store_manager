from typing import Any
from django.contrib import admin
from django.db.models import Sum

from payments.models import Provider, SalesBill
from sales.models import Utility
from payments.forms import ProviderForm


# Register your models here.
@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['company_display','bill','createdAt','value']
    date_hierarchy = 'createdAt'
    search_fields = ("bill__number",)
    ordering = ('createdAt',)
    
    form = ProviderForm

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
    
