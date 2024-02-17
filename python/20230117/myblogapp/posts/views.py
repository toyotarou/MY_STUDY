from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
#    return HttpResponse("Hellow World")

    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})
#
def post_detail(request, post_id):
    return render(request, 'posts/post_detail.html', {'post_id':post_id})
