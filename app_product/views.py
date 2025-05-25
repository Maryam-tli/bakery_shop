from django.shortcuts import render, get_object_or_404
from app_product.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def home_shop_view(request, cat_slug = None):
    products = Product.objects.filter(status=0, available=True)
    categories = Pro_Category.objects.all()
    categories_dict = {}
    for item in categories:
        categories_dict[item] = Product.objects.filter(status=0, available=True, pro_category = item).count()
        
    selected_category = None
    if cat_slug:
        selected_category = get_object_or_404(Pro_Category, slug=cat_slug)
        products = products.filter(pro_category=selected_category)


    p = Paginator(products, 9)
    try:
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context={'page_obj' : page_obj, 'categories' : categories_dict, 'selected_category' : selected_category}
    return render(request, 'product-list.html', context)


def detail_shop_view(request, slug):
    class_prod = get_object_or_404(Product, slug=slug, status=0, available=True)
    products = list(Product.objects.filter(status=0, available=True).order_by('-created'))
    try:
      index = products.index(class_prod)
    except ValueError:
      index = -1

    if index<0:
        index = 0
    elif index >= len(products):
        index = len(products) - 1
    
    if index > 0:
        prev_post = products[index - 1]
    else:
        prev_post = None

    if index < len(products) - 1:
        next_post = products[index + 1]
    else:
        next_post = None
        
    context = {'class_prod' : class_prod, 'prev_post': prev_post, 'next_post': next_post,}
    return render(request, 'product-detail.html', context)