from django.urls import path
from provider.views import BillDetailView

urlpatterns = [
    # path('pays/b/<int:pk>', BillDetailView.as_view(), name='detail-pay'),
    path('bill/<int:pk>/detail', BillDetailView.as_view(), name='bill-detail'),
]
