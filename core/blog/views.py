from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class ListaDePost(ListView):
    model = Post
    queryset = Post.objects.filter(publicado=True).order_by('-data_criacao')
    paginate_by = 10


class PostDetalhado(DetailView):
    model = Post
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
