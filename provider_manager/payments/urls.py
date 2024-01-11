from django.urls import path
from payments.views import ProviderDetailView

urlpatterns = [
    path('b/<int:pk>', ProviderDetailView.as_view(), name='bill-pay'),
]
