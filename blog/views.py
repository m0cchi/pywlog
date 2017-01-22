from django.http import HttpResponse
from django.template.loader import render_to_string
# from django.shortcuts import render
from .models import Article, TagMapper

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

    rendered = render_to_string('blog/article.html', {'article': article,
                                                      'tags': ', '.join(map((lambda mapper: mapper.tag.name),
                                                                            mappers))})
    return HttpResponse(rendered)
