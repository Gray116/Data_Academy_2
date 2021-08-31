from django.shortcuts import render
# DB 액세스한 것과 같다.
from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

# def index(request):
#     object_list = Post.objects.all()
#     context = {'object_list':object_list}
#     return render(request, 'blog/post_list.html', context)


def detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'blog/detail.html', {'post':post})