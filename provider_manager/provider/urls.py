from django.urls import path
from provider.views import BillDetailView, BillPayView

urlpatterns = [
    path('b/<int:pk>/detail', BillDetailView.as_view(), name='bill-detail'),
    path('bill/<int:pk>/pay',BillPayView.as_view(), name='bill-pay'),
]
