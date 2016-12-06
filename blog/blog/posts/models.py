from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from redactor.fields import RedactorField

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(u'Titulo', max_length=100)
    conteudo = RedactorField(u'Conteudo')
    data_post = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User)
    tags = models.CharField(u'Tags', max_length=30)
    categoria = models.ForeignKey('Categoria')
    slug = AutoSlugField(populate_from='titulo')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-id']

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(u'Categoria', max_length=100)
    obs = models.TextField(u'Observacao', blank=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering = ['id']

    def __str__(self):
        return self.nome
