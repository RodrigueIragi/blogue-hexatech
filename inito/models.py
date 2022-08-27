from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from content_editor.models import Region, create_plugin_base
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    desc = RichTextField(blank=True, null=True)
    image = models.FileField(upload_to='article', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_updaload = RichTextUploadingField(blank=True, null=True)
    
    regions = [
        Region(key='main', title='main region'),
        Region(key='sidebar', title='sidebar region')
    ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse("my-articles")


    # create_plugin_base does nothing outlandish, it only defines an
    # abstract base model with the following attributes:


ArticlePlugin = create_plugin_base(Article)

class RichText(ArticlePlugin):
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'rich text'
        verbose_name_plural = 'rich texts'

class Download(ArticlePlugin):
    file = models.FileField(upload_to='downloads/%Y/%m/')
    
    class Meta:
        verbose_name = 'download'
        verbose_name_plural = 'downloads'
