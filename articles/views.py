from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm, CommentForm
from .models import Article
from django.contrib.auth.models import User

@login_required
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
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'retrieve.html', context)

def about(request):
    return render(request, 'about.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
    return render(request, 'login.html')
