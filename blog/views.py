from django.shortcuts import render_to_response
from django.http import Http404
from mysite.blog.models import Blog
from mysite.blog.models import Comment

def index(request):
    blog_posts = Blog.objects.all().order_by('-pub_date')[:5]
    return render_to_response('blog/index.html', {'blog_posts': blog_posts})

def post(request,blog_id):
    try:
        post = Blog.objects.get(pk=blog_id)
        #Below, I want to get the comments
        #----------------------------------------------------------
        comments = Comment.objects.filter(blog=post)
        #----------------------------------------------------------

    except Blog.DoesNotExist:
        raise Http404
    return render_to_response('blog/post.html', {'post': post, 'comments': comments})