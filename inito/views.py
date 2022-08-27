import email
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article
from app_admin.models import Comment
from app_admin.forms import CommentForm, EmailForm
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.method == 'POST':
        comment_form = EmailForm(data=request.POST)
        if comment_form.is_valid:
            comment_form.save()
            messages.success(request, 'Souscription Reussi, Vous serrez informer de toutes les nouvelles !')
            print('Email envoyé !')
            return redirect('/')
            
    else:
        comment_form = EmailForm()
        print('Non creer !')
            
            
    return render(request, 'index.html', {'form':comment_form})


def about(request):

    return render(request, 'apps/about.html')
def blog(request):

    return render(request, 'apps/blog.html')

def article(request):
    if request.method == 'GET':

        list_articles = Article.objects.all()
        context = {'list_articles': list_articles}

        return render(request, 'apps/article.html', context)

def detail(request, id_article):
    article = Article.objects.get(id=id_article)
    user = User.objects.all()

    category = article.category
    articles_relation = Article.objects.filter(category=category)[:5]
    comments = Comment.objects.filter(article=article.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid:
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
    else:
        comment_form = CommentForm()
    

    return render(request, 'apps/detail.html', {"article": article, 
                                                'aer':articles_relation,
                                                'comments':comments,
                                                'new_comment':new_comment,
                                                'comment_form':comment_form})


def search(request):
    query = request.GET['article']
    list_article = Article.objects.filter(title__contains=query)
    counter = list_article.count()
    return render(request, 'apps/search.html', {'query':query,'list_article': list_article, "counter":counter})