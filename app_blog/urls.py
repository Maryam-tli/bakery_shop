from django.urls import path
from app_blog.views import *

urlpatterns = [
    path('', blog_home_view, name='blog'),
    path('<slug:slug>/', blog_detail_view, name='detail'),
]