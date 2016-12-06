from django.conf.urls import url

from . import views

app_name = 'sobre'

urlpatterns = [
	url(r'^$', views.sobre_nos, name='sobre-nos'),
]