from django.urls import path
from sales.views import OrderDetailView

urlpatterns = [
    path('invoice/<int:pk>', OrderDetailView.as_view(), name='invoice-detail'),
]
