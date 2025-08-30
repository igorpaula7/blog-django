from django.urls import path
from blog.views import ListaDePost, PostDetalhado

urlpatterns = [
    path('list/', ListaDePost.as_view(template_name='post_list.html')),
    path('list/<slug:slug>/', PostDetalhado.as_view(template_name='base_post.html'), name = 'post-detalhado')
]
