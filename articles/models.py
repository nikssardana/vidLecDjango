from django.db import models

class Article(models.Model):
    title = models.TextField(max_length=254)
    body = models.TextField()
    likes = models.IntegerField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField()
