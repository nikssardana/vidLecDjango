from django.db import models
from time import time

def get_upload_filename(instance,filename):
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)

class Article(models.Model):
    title = models.TextField(max_length=254)
    body = models.TextField()
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to = get_upload_filename,blank=True,null=True)
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField()
