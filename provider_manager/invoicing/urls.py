from django.urls import path

from invoicing.views import InvoiceCreateView
from sales.views import SearchClientListView, clientView

urlpatterns = [
    path('', InvoiceCreateView.as_view(), name='invoice'),
    path('search/client/', SearchClientListView, name='search-client'),
    path('client/', clientView, name='client'),
]
