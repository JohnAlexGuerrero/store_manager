import pandas as pd

from django.contrib import admin
from django.db.models import Sum
from decimal import Decimal
from datetime import datetime

from inventory.models import Product, Category
from inventory.forms import CategoryForm, ProductForm

# Register your models here.
def report_cost_items(modeladmin, request, queryset):
    data = {
        'codigo':[x.code for x in queryset],
        'producto':[x.description for x in queryset],
        'stock':[x.stock for x in queryset],
        'unidad':[x.unit for x in queryset],
        'valor unitario':[x.cost_with_tax for x in queryset],
        'valor total':[Decimal(x.cost_with_tax * x.stock) for x in queryset],
    }
    
    df = pd.DataFrame(data)
    print(df)
    df.to_excel(f"{datetime.now().strftime("%Y-%m-%d")}.xlsx",
        sheet_name='electricidad'
    )
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","items","total_cost_items"]
    form = CategoryForm
    
    def total_cost_items(self, obj):
        total_cost = 0
        items = Product.objects.filter(category__id=obj.id)
        for item in items:
            total_cost += (item.cost_with_tax * item.stock)
        return f'$ {total_cost:,.2f}'
        
    def items(self, obj):
        return Product.objects.filter(category__id=obj.id).count()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','description','stock','unit','price','total_cost_stock','category_display']    
    list_editable = ('stock',)
    search_fields = ['description','category__name']
    # list_filter = ['category_display']s
    list_per_page = 10
    ordering = ('description',)
    form = ProductForm
    
    def category_display(self, obj):
        categories = Category.objects.filter(products__id=obj.id)
        categories_arr = [c.name for c in categories]
        return categories_arr
    
    def total_cost_stock(self, obj):
        return f'$ {(obj.cost_with_tax * obj.stock):,.2f}'
    
    def price(self, obj):
        return f'$ {round(obj.cost_with_tax,0):,.2f}'
    
    admin.site.add_action(report_cost_items, 'Reporte de costos')
    
