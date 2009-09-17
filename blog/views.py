from django.shortcuts import render_to_response
from mysite.blog.models import Blog

def index(request):
    blog_posts = Blog.objects.all().order_by('-pub_date')[:5]
    return render_to_response('blog/index.html', {'blog_posts': blog_posts})