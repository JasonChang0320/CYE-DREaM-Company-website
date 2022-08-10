from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def showtemplate(request):
    return render(request, 'post.html')

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'Post_list'
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'