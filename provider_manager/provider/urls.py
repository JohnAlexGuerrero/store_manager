from django.urls import path
from provider.views import BillDetailView, ProviderCreateView

urlpatterns = [
    path('b/<int:pk>/detail', BillDetailView.as_view(), name='bill-detail'),
    path('bill/<int:pk>/pay', ProviderCreateView.as_view(), name='bill-pay'),
]
