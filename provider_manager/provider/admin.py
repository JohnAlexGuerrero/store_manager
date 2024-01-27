from django.contrib import admin
from django.db.models import Sum
from datetime import datetime
from django.shortcuts import redirect

from provider.models import Company, Bill, OrderDetail
from payments.models import Provider

from payments.forms import ProviderForm

# Register your models here.
def selected_one_bill(modeladmin, request, queryset):
    if queryset.count() == 1:
        item = queryset.first()
        return item
    else:
        modeladmin.message_user(request, "Por favor selecciona una sola cuenta")
        

def view_bill(modeladmin, request, queryset):
    item = selected_one_bill(modeladmin, request, queryset)
    if item:
        return redirect('bill-detail', pk=item.id)
    

# pay_bill.short_description = "Pagar"
view_bill.short_description = "Ver"
    
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','sellerman','phone','balance_total']
    fields = ['name', 'address','phone','sellerman']
    
    def balance_total(self, obj):
        total = Bill.objects.filter(company__name=obj.name).aggregate(Sum('total'))
        return f'$ {total['total__sum']:,.2f}'

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['company_display','number','createdAt','expirationAt','way_to_pay','total','status','balance_total']
    search_fields = ['number',]
    list_filter = ("company__name",)
    list_per_page = 10
    date_hierarchy = 'createdAt'
    actions = [view_bill]

    
    '''crear accion de pago de factura'''
    def pay_bill(modeladmin, request, queryset):
        item = selected_one_bill(modeladmin, request, queryset)
        if item:
            # form = ProviderForm(
            #         user=request.user.username,
            #         bill=item.number,
            #         value=item.total,
            #         description='',
            #         createdAt=datetime.now().strftime("%Y-%m-%d")
            #     )
            # print(form)
            return redirect('bill-pay', pk=item.id)
        modeladmin.message_user(request, 'La factura fue cancelada')
        
    def balance_total(self, obj):
        pays = Provider.objects.filter(bill__number=obj)
        if pays:
            return f'$ {obj.total - pays.aggregate(Sum('value'))['value__sum']:,.2f}'
        return f'$ {0.0}'
    
    def company_display(self, obj):
        return obj.company
    
    def status(self, obj):
        if obj.is_paid:
            return 'Cancel'
        
        return 'Pending'
    
    admin.site.add_action(pay_bill, 'Pago total')


    
@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['createdAt','product_display','quantity','unit_display','price']
    
    def product_display(self, obj):
        return obj.product

    def unit_display(self, obj):
        return obj.product.unit
    
