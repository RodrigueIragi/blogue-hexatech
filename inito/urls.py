from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('article', views.article, name='article'),
    path('article/recherche', views.search, name='search'),
    path('article/<int:id_article>', views.detail, name='detail'),
]