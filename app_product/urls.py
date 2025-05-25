from django.urls import path
from app_product.views import *

urlpatterns = [
    path('',home_shop_view, name = 'shop'),
    path('category/<slug:cat_slug>/', home_shop_view, name = 'category'),
    path('product-detail/<slug:slug>/', detail_shop_view, name = 'detail'),
]