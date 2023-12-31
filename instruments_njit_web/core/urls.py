"""
URL configuration for instruments_njit_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import (
    HomeView,
    ItemDetailView
    )
from .views import add_to_cart
from .views import remove_from_cart
# from .views import item_list
from .views import checkout
from .views import thankyou
app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('checkout.html', checkout, name='checkout'),
    path('thank-you.html', thankyou, name='thank_you'),
]

