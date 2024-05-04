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
        Q(description__icontains=query)
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
    

class InventoryView(TemplateView):
    template_name = "inventory/index.html"
