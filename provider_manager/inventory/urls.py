from django.urls import path
from inventory.views import InventoryView

urlpatterns = [
    path('<slug:slug_name>/', InventoryView.as_view(),name='collections'),
]
