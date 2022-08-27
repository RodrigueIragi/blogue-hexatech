from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

admin.site.register(Blog, BlogAdmin)