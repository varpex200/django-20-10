# Generated by Django 4.1.1 on 2022-10-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default='', upload_to='article-thumbnails', verbose_name='تصویر'),
        ),
    ]
