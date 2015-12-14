from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
    url(r'^all/$','articles.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$','articles.views.article'),
    url(r'^create/$','articles.views.create'),
    url(r'^like/(?P<article_id>\d+)/$','articles.views.like_article'),
)
