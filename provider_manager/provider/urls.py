from django.urls import path
from provider.views import BillDetailView, BillPayView, ProviderListView

urlpatterns = [
    path('b/<int:pk>/detail', BillDetailView.as_view(), name='bill-detail'),
    path('bill/<int:pk>/pay',BillPayView.as_view(), name='bill-pay'),
    path('bill/dashboard', ProviderListView.as_view() ,name='index')
]
