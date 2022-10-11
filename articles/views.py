from django.shortcuts import render
from django.http.response import HttpResponse

from articles.forms import ArticleForm
from .models import Article
from django.contrib.auth.models import User


def index(request):
    user = User.objects.get(id=2)
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()
    articles = Article.objects.filter()
    context = {
        'articles': articles,
        'form': form
    }
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'retrieve.html', context)

def about(request):
    return render(request, 'about.html')