from django import forms
from django.db.models import Q

from inventory.models import Category
from inventory.models import Product

def set_code_bar():
    return f'{Product.objects.all().count() + 1020002}'

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ("name","products")
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__( *args, **kwargs)
        
        if kwargs.values():
            print(kwargs.keys())
            print(kwargs.values())
            x = kwargs.values()
            print(x)
        # if kwargs is not None:
        #     category = Category.objects.get(name=kwargs['instance'])
        #     print(category)
        #     self.fields['products'].queryset = Product.objects.filter(category__name=category)

class ProductForm(forms.ModelForm):
    code = forms.CharField(initial=set_code_bar)
    class Meta:
        model = Product
        fields = ("description","code","stock","unit","cost","tax","cost_with_tax","updatedAt")

