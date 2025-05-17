from django.shortcuts import render, get_object_or_404
from app_blog.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def blog_home_view(request):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    p = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.get_page(1)
    except EmptyPage:
        page_obj = p.get_page(p.num_pages)

    context={'page_obj' : page_obj}
    return render(request, 'blog-home.html', context)

def blog_detail_view(request, slug):
    class_post = get_object_or_404(Post, slug=slug, status=True, published_date__lte=timezone.now())
    class_post.counted_views += 1
    class_post.save(update_fields=['counted_views'])
    posts = list(Post.objects.filter(published_date__lt=timezone.now()).order_by('-published_date'))
    try:
      index = posts.index(class_post)
    except ValueError:
      index = -1

    if index<0:
        index = 0
    elif index >= len(posts):
        index = len(posts) - 1
    
    if index > 0:
        prev_post = posts[index - 1]
    else:
        prev_post = None
    if index < len(posts) - 1:
        next_post = posts[index + 1]
    else:
        next_post = None
    context = {'class_post' : class_post}
    return render(request, 'blog-detail.html')