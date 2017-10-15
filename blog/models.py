from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=24)
    password = models.CharField(max_length=16)

    @classmethod
    def register(cls, name, password):
        Author(name=name, password=password).save()

    def publish(self, article):
        article.author = self
        article.save()


class Article(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=128)
    content = models.CharField()

    @classmethod
    def get_all(cls):
        articles = []
        for article in Article.objects.all():
            articles.append(article)
        return articles
