"""shopping_cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from apps.base.views import IndexView, UserView, LoginView, SettingsView
from apps.order.views import OrderDetail
from django.conf import settings
from django.conf.urls.static import static
import os

from .routers import urlpatterns as urlpatterns_routers


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path(r'api/v1/', include(urlpatterns_routers)),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/signup/', UserView.as_view(), name="signup"),
    path('shopping_cart/', OrderDetail.as_view(), name="index"),
    path('product/', include('apps.product.urls')),
    path('order/', include('apps.order.urls')),
    path('shipment/', include('apps.shipment.urls')),
    path('payment/', include('apps.payment.urls')),
    path('settings/', SettingsView.as_view(), name="settings"),
]


if os.environ.get("DEBUG"):
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
