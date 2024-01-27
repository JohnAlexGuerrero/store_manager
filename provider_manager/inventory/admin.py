from django.contrib import admin
from inventory.models import Product, Category
from inventory.forms import CategoryForm, ProductForm

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","items"]
    form = CategoryForm
    
    def items(self, obj):
        return Product.objects.filter(category__id=obj.id).count()


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code','description','stock','price','total_cost_stock','category_display']    
    search_fields = ['description']
    # list_filter = ['category_display']
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
    
