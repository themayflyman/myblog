"""myblog URL Configuration

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
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include("markdownx.urls")),
    url(r'^ckeditor/', include("ckeditor_uploader.urls")),
    # url(r'^(?P<slug>\S+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^', include("blog.urls")),
    url(r'^comment/(?P<slug>\S+)/approve', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<slug>\S+)/remove', views.comment_remove, name='comment_remove'),
    # url(r'^comments/', include('django_comments.urls')),
    url(r'^comments/', include('fluent_comments.urls')),
]
