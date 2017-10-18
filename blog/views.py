from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from blog.models import Article, Author


def blog_index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def index(request):
    return HttpResponse("Global index page")


def get_article(request, article_id):
    article = Article.objects.all().filter(id=article_id)[0]
    return render(request, 'blog/article.html', {'article': article})


def get_author(request, author_id):
    author = Author.objects.all().filter(id=author_id)[0]
    return HttpResponse(author.name)

