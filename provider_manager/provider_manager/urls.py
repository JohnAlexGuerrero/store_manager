
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', admin.site.urls),
    path('sales/', include('sales.urls')),
    path('collections/', include('inventory.urls')),
    path('providers/', include('provider.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('invoicing/', include('invoicing.urls')),
]
