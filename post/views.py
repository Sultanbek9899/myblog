from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.


def post_list(request):
    post=Post.published.all()
    print(post)
    return render(request, 'list.html', context={'posts':post})


def post_detail(request,post):
    post= get_object_or_404(Post, slug=post, status='published')
    return render(request, 'detail.html', {'post':post})