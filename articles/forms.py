from django.forms import ModelForm
from .models import *


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'related_user', 'thumbnail']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'