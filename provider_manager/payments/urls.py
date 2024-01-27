from django.urls import path
from payments.views import ProviderCreateView

urlpatterns = [
    path('create', ProviderCreateView.as_view(), name='create-pay-provider'),
]
