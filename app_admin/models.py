from django.db import models
from inito.models import Article
from django.contrib.auth.models import User
# Create your models here.
class Comment(models.Model):
    name_post = models.CharField(max_length=200, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_post +"    /"+ self.article.title

class EmailNewsletter(models.Model):
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email