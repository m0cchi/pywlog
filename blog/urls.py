from django.conf.urls import url
from .views.show import show_article, show_articles, export_db

urlpatterns = [
    url(r'^$', show_articles, name='index'),
    url(r'^article/$', show_article, name='article'),
    url(r'^export/$', export_db, name='article'),
]
