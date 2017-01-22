from django.conf.urls import url
from .views import show_article, show_articles

urlpatterns = [
    url(r'^$', show_articles, name='index'),
    url(r'^article$', show_article, name='article'),
]
