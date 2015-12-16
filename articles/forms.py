from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','body','thumbnail') #fields that must be rendered in the form, rest are hidden in a way
