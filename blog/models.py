from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length = 25)
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 25)
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    create_user = models.ForeignKey(User, related_name='article_create_user')
    update_date = models.DateTimeField(auto_now = True)
    update_user = models.ForeignKey(User, related_name='article_update_user')
    def __str__(self):
        return '{} {}'.format(self.title, self.create_date)

class TagMapper(models.Model):
    tag = models.ForeignKey(Tag)
    article = models.ForeignKey(Article)
    def __str__(self):
        return '{} {}'.format(self.article.title, self.tag.name)
    class Meta:
        unique_together = (('tag', 'article'))
