from django.urls import path
from sales.views import OrderView

urlpatterns = [
    path('invoice/', OrderView.as_view(), name='sales-invoice'),
]
