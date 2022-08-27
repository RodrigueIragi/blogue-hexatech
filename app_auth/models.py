from django.db import models
from ckeditor.fields import RichTextFormField, RichTextField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=123)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title