from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from pages.models import Post


def links_view(request):
    return render(request,'links.html')

def resume_view(request):
    return render(request,'resume.html')

def base_view(request):
    return render(request, '_base.html')

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    slug_field = 'url'