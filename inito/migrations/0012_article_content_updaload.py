# Generated by Django 4.0.6 on 2022-08-26 15:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inito', '0011_remove_comment_article_remove_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_updaload',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
