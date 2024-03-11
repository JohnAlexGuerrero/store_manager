from django.urls import path
from dashboard.view import HomeView, SearchDateView

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('date/', SearchDateView.as_view(), name='search_per_date'),
]
