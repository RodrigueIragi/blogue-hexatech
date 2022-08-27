# Generated by Django 4.0.6 on 2022-08-25 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inito', '0008_emailnewsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailnewsletter',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.CreateModel(
            name='RichText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('text', models.TextField(blank=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_set', to='inito.article')),
            ],
            options={
                'verbose_name': 'rich text',
                'verbose_name_plural': 'rich texts',
            },
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to='downloads/%Y/%m/')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_set', to='inito.article')),
            ],
            options={
                'verbose_name': 'download',
                'verbose_name_plural': 'downloads',
            },
        ),
    ]
