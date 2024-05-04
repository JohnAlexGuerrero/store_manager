from django.urls import path

from invoicing.views import InvoiceCreateView
from sales.views import SearchClientListView, clientView
from inventory.views import searchProduct, selectProduct

urlpatterns = [
    path('', InvoiceCreateView.as_view(), name='invoice'),
    path('search/client/', SearchClientListView, name='search-client'),
    path('client/', clientView, name='client'),
    path('search/product/', searchProduct, name='search-product'),
    path('product/', selectProduct, name='product'),
]
