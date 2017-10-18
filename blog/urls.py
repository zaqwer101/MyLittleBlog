from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog_index, name='blog_index'),
    url(r'^(?P<article_id>[0-9]+)/$', views.get_article, name="article_detail"),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.get_author, name="author_detail")

]