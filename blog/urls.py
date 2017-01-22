from django.conf.urls import url
from .views import show_article

urlpatterns = [
    url(r'^$', show_article, name='index'),
]
