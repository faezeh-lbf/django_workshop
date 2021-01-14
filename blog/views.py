from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost


def get_all_posts(request):
    posts = BlogPost.objects.order_by('-publish_date')
    output = {
        'posts': posts
    }

    return render(request, 'blog/index.html', output)

