from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    data_criacao = models.DateTimeField(auto_now_add=True)
    publicado = models.BooleanField(default=False, verbose_name='Publicado')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.titulo