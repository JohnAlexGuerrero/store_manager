from django.urls import path
from sales.views import (
    OrderDetailView, pdfReportSales, ShopingCartView,
    SearchSalesByMonthView
)


urlpatterns = [
    path('invoice/<int:pk>', OrderDetailView.as_view(), name='invoice-detail'),
    path('cart/', ShopingCartView.as_view(), name="cart"),
    path('report/pdf', pdfReportSales, name='report-sales'),
    path('search/', SearchSalesByMonthView.as_view(), name="search-month"),
]
