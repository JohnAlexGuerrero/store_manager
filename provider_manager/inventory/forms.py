from django import forms
from inventory.models import Category
from inventory.models import Product

def set_code_bar():
    return f'{Product.objects.all().count() + 1020002}'

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ("name","products")
        
    def get_items_with_category():
        products = Product.objects.all()
        return []

class ProductForm(forms.ModelForm):
    code = forms.CharField(initial=set_code_bar)
    class Meta:
        model = Product
        fields = ("description","code","stock","unit","cost_with_tax","updatedAt")
