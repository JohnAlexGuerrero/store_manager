from django.urls import path
from dashboard.view import HomeView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
]
