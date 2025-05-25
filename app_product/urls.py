from django.urls import path
from app_product.views import *

urlpatterns = [
    path('',home_shop_view, name = 'shop'),
    path('product-detail/<slug:slug>/', detail_shop_view, name = 'detail'),
]