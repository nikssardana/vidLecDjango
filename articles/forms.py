from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = [] #fields or exclude variable must be specified
