from django.urls import path
from sales.views import OrderDetailView, pdfReportSales

urlpatterns = [
    path('invoice/<int:pk>', OrderDetailView.as_view(), name='invoice-detail'),
    path('report/pdf', pdfReportSales, name='report-sales'),
]
