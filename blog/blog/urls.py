"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blog.core import urls as core_urls
from blog.sobre import urls as sobre_urls
from blog.posts import urls as posts_urls
from blog.contato import urls as contato_urls

app_name = 'blog'

urlpatterns = [
	url(r'', include(core_urls, namespace='core')),
	url(r'^sobre/', include(sobre_urls, namespace='sobre')),
	url(r'^posts/', include(posts_urls, namespace='posts')),
	url(r'^contato/', include(contato_urls, namespace='contato')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
