from django.conf.urls import url

from . import views

app_name = 'contato'

urlpatterns = [
    url(r'^$', views.contato, name='contato'),
]
