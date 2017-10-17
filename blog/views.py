from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from blog.models import Article


def blog_index(request):
    return HttpResponse("Look at my blog, my blog is amazing")


def index(request):
    return HttpResponse("Global index page")


def get_article(request, article_id):
    article = Article.objects.all().filter(id=article_id)[0]
    return HttpResponse(str(article.title) + "<br>" + article.content)