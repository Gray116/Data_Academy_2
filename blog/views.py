from django.shortcuts import render
# DB 액세스한 것과 같다.
from .models import Post


def index(request):
    post = Post.objects.all()
    context = {'posts':post}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'blog/detail.html', {'post':post})