from pydoc import visiblename
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_form, name="login"),
    path('register', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('account_user', views.account_user, name='account_user')
]