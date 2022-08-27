from django.shortcuts import render, redirect
from inito.models import Article
from inito.forms import ArticleForm
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView, DeleteView, CreateView
# Create your views here.
@login_required
def dashboard(request):
    has_perm = False
    if request.user.has_perm('portefolio.delete_article'):
        has_perm = True
        print('il peut supprimer')
    else:
        raise PermissionDenied
        
    return render(request, 'db.html')

@login_required
def user_articles(request):
   # if not request.user.is_authenticated:

       # return redirect('/')
    has_perm = False
    if request.user.has_perm('portefolio.delete_article'):
        has_perm = True
        print('il peut supprimer')
    else:
        raise PermissionDenied

    list_articles = Article.objects.filter(user=request.user)

    return render(request, 'my-articles.html', {'list_articles': list_articles})

def ajouter_article(request):
    pass

class AddArticle(LoginRequiredMixin,CreateView):

    model = Article
    form_class = ArticleForm
    template_name = 'add-article.html'
    success_url = '/my-admin/my-articles'

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)

class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app_admin/article_form.html'

class DeleteArticle(LoginRequiredMixin,DeleteView):
    model = Article
    success_url = '/my_admin/my-articles'