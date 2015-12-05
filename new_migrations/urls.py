from django.conf.urls import include, url
from django.contrib import admin
from articles.views import HelloTemplate

urlpatterns = [
    # Examples:
    # url(r'^$', 'new_migrations.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$','articles.views.hello'),
    url(r'^hello_template/$','articles.views.hello_template'),
    url(r'^hello_class_view/$',HelloTemplate.as_view()),
    url(r'^hello_template_simple/$','articles.views.hello_template_simple'),
    url(r'^$','articles.views.index'),
    
    url(r'^articles/',include('articles.urls')),

    url(r'^base/$','articles.views.base'),
    url(r'^base/extended$','articles.views.extendedTemplate'),

    url(r'^language/(?P<language>[a-z\-]+)/$','articles.views.language'),
    #\- is for '-' eg in en-gb

    url(r'^accounts/login/$','new_migrations.views.login'),
    url(r'^accounts/auth/$','new_migrations.views.auth_view'),
    url(r'^accounts/logout/$','new_migrations.views.logout'),
    url(r'^accounts/loggedin/$','new_migrations.views.loggedin'),
    url(r'^accounts/invalid/$','new_migrations.views.invalid_login'),

]
