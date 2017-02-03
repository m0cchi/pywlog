from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article, TagMapper
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os

def show_article(request):
    article_id = request.GET['article_id'] if 'article_id' in request.GET else None
    article = None
    mappers = []
    try:
        article_id = int(article_id)
        article = Article.objects.get(id = article_id)
        mappers = TagMapper.objects.filter(article = article)
    except:
        # render 404
        pass

    rendered = render(request,
                      'blog/show/article.html',
                      {'article': article,
                       'tags': ', '.join(map((lambda mapper: mapper.tag.name),
                                             mappers))})
    return HttpResponse(rendered)

def show_articles(request):
    page_id = request.GET['page_id'] if 'page_id' in request.GET else None
    paginator = Paginator(Article.objects.all().order_by('-id'), settings.SHOW_COUNT)
    page = None
    try:
        page = paginator.page(page_id)
    except (EmptyPage, PageNotAnInteger):
        page = paginator.page(1)

    rendered = render(request,
                      'blog/show/article-list.html',
                      {'articles': page.object_list,
                       'page': page})

    return HttpResponse(rendered)

@login_required
def export_db(request):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sqlite = os.path.join(root, 'db.sqlite3') # sqlite
    file = open(sqlite, 'rb')
    response = HttpResponse(file)
    response['content_type'] = 'application/x-sqlite3'
    response['Content-Disposition'] = 'attachment; filename=export.sqlite3'
    return response
    
