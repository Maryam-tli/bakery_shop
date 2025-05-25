from django.shortcuts import render, get_object_or_404
from app_product.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home_shop_view(request):
    products = Product.objects.filter(status=0, available=True)
    p = Paginator(products, 9)
    try:
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context={'page_obj' : page_obj}
    return render(request, 'product-list.html', context)