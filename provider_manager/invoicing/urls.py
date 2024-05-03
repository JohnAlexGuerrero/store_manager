from django.urls import path

from invoicing.views import InvoiceCreateView
from sales.views import SearchClientListView

urlpatterns = [
    path('', InvoiceCreateView.as_view(), name='invoice'),
    path('search/client/', SearchClientListView, name='search-client'),
]
