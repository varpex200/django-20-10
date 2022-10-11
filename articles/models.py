from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ ایجاد')

    class Meta:
        abstract = True


# Create your models here.
class Article(BaseModel):
    title = models.CharField(max_length=128, verbose_name='عنوان')
    thumbnail = models.ImageField(upload_to='article-thumbnails', blank=True, default='')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مفاله ها'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField(verbose_name='متن')
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر مربوطه')
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله مربوطه')

    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'