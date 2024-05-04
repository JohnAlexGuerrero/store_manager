from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse

from django.views.generic import TemplateView

from inventory.models import Product

# Create your views here.

#filtrar los productos segun su descripcion
def searchProduct(request):
    query = request.GET.get('q')
    
    products = Product.objects.filter(
        Q(description__contains=query)
    )
    
    return JsonResponse({
        "items": [
            {
                "id": item.id,
                "description": item.description,
                "code": item.code,
                "und": item.unit,
                "stock": item.stock,
                "tax": item.tax,
                "price": item.cost_with_tax,
            }
            for item in products
        ]
    })

#seleccion de producto
def selectProduct(request):
    code = request.GET.get('q')
    
    item = Product.objects.get(code=code)
    print(item)
    
    return JsonResponse({
        "item":[
            {
                "id": item.id,
                "description": item.description,
                "code": item.code,
                "und": item.unit,
                "stock": item.stock,
                "tax": item.tax,
                "price": item.cost_with_tax,
            }
        ]
    })
    

class InventoryView(TemplateView):
    template_name = "inventory/index.html"
