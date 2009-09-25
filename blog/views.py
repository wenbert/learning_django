from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import Count
from mysite.blog.models import Blog
from mysite.blog.models import Comment
from mysite.blog.forms import CommentForm
import datetime

def index(request):
    blog_posts = Blog.objects.all().annotate(Count('comment')).order_by('-pub_date')[:5]
    
    return render_to_response('blog/index.html', 
                             {'blog_posts': blog_posts})

def post(request,blog_id):
    try:
        blogpost = Blog.objects.get(pk=blog_id)
        comments = Comment.objects.filter(blog__pk=blog_id)
        comment_count = comments.count()
        
        if request.method != 'POST' :
            comment_form = CommentForm()
        else:
            errors = []
            initial_values = {}
            if not request.POST['author']:
                errors.append('Enter your name.')
                initial_values = {'comment':request.POST['comment'], 'url': request.POST['url']}
            elif not request.POST['comment']:
                errors.append('Enter a comment.')
                initial_values = {'author':request.POST['author'], 'url': request.POST['url']}
            else:
                comment = Comment()
                comment.blog_id  = blog_id
                comment.author   = request.POST['author']
                comment.email   = request.POST['email']
                comment.comment  = request.POST['comment']
                comment.url      = request.POST['url']
                comment.pub_date = datetime.datetime.now()
                comment.save()
                return HttpResponseRedirect('/blog/post/'+blog_id)
            
            comment_form = CommentForm(initial=initial_values)
            
            return render_to_response('blog/post.html',
                                      {'blogpost': blogpost, 
                                      'comments': comments, 
                                      'comment_count': comment_count,
                                      'comment_form': comment_form,
                                      'errors': errors})
    except Blog.DoesNotExist:
        raise Http404            
    
    return render_to_response('blog/post.html', 
                             {'blogpost': blogpost, 
                              'comments': comments, 
                              'comment_count': comment_count,
                              'comment_form': comment_form})
        

    


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))