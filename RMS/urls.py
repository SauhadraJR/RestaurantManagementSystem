"""
URL configuration for RMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff-management/',include('staff_management.urls')),
    path('table-management/',include('table_management.urls')),
    path('user-management/',include('user_management.urls')),
    path('order-management/',include('order_management.urls')),
    path('menu-management/',include('menu_management.urls')),
    path('inventory-management/',include('inventory_management.urls')),
    path('kitchen-display/',include('kitchen_display.urls')),
    path('accounting/',include('accounting.urls')),
]
