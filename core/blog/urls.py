from django.urls import path
from blog.views import ListaDePost, PostDetalhado

urlpatterns = [
    path('', ListaDePost.as_view(template_name='post_list.html')),
    path('<slug:slug>/', PostDetalhado.as_view(template_name='post_detail.html'), name = 'post-detalhado')
]
