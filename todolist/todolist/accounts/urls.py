from django.conf.urls import url

from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', views.home, name='home'),
    url(r'^cadastro/$', views.register, name='register'),
    url(r'^fazer-login/$', views.user_login, name='user-login'),
    url(r'^logado/$', views.logado, name='logado'),
    url(r'^sair/$', views.sair, name='sair'),
]
