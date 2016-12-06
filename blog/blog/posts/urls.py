from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^ler-post/(?P<slug>[\w-]+)/$', views.ler_post, name='ler-post'),
    url(r'^categoria/(?P<id_categoria>[0-9]+)/$', views.lista_posts_categoria, name='lista-posts-categoria'),
]
