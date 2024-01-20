from django.contrib import admin
from django.db.models import Sum
from provider.models import Company, Bill, OrderDetail
from payments.models import Provider
from payments.views import ProviderDetailView
from django.shortcuts import redirect

# Register your models here.
def selected_one_bill(modeladmin, request, queryset):
    if queryset.count() == 1:
        item = queryset.first()
        return item
    else:
        modeladmin.message_user(request, "Por favor selecciona una sola cuenta")
        
def pay_bill(modeladmin, request, queryset):
    item = selected_one_bill(modeladmin, request, queryset)
    if item:
        return redirect('detail-pay', pk=item.id)

def view_bill(modeladmin, request, queryset):
    item = selected_one_bill(modeladmin, request, queryset)
    if item:
        return redirect('bill-detail', pk=item.id)
    

pay_bill.short_description = "Pagar"
view_bill.short_description = "Ver"
    
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','sellerman','phone','balance_total']
    fieldsets = (
        (
            None,
            {
                "fields":['name','sellerman','phone'],
            }
        ),
        (
            "Info Optionals",
            {
                "classes":["collapse"],
                "fields":['address']
            }
        )
    )
    
    def balance_total(self, obj):
        total = Bill.objects.filter(company__name=obj.name).aggregate(Sum('total'))
        return f'{total['total__sum']:,.2f}'

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['company_display','number','createdAt','expirationAt','way_to_pay','total','status','balance_total']
    search_fields = ['number',]
    list_filter = ("company__name",)
    actions = [pay_bill, view_bill]
    
        
    def balance_total(self, obj):
        pays = Provider.objects.filter(bill__number=obj)
        if pays:
            return f'$ {obj.total - pays.aggregate(Sum('value'))['value__sum']:,.2f}'
        return f'$ {0.0}'
    
    def company_display(self, obj):
        return obj.company
    
    def status(self, obj):
        bill_obj = Bill.objects.get(number=obj.number)
        pay = Provider.objects.filter(bill=bill_obj.id).aggregate(Sum('value'))
        
        if pay['value__sum'] == None:
            return 'Pending'
        
        balance = bill_obj.total - pay['value__sum']
        return 'Saldo' if balance > 1000 else 'Cancel'
    



    
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['createdAt','product_display','quantity','unit_display','price']
    
    def product_display(self, obj):
        return obj.product

    def unit_display(self, obj):
        return obj.product.unit
    
