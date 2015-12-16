from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context,Template
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article
from .forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def hello(request):
    name = "Nikhil"
    html = '<html><body>Hi %s. It seems to have worked!</body></html>'%name
    return HttpResponse(html)

def hello_template(request):
    name = 'Nikhil'
    t = get_template('hello.html')
    html = t.render(Context({'name':name}))
    return HttpResponse(html)

class HelloTemplate(TemplateView):  #class based view, a view that knows how to render itself
    template_name = 'hello_class.html'

    def get_context_data(self,**kwargs):
        context = super(HelloTemplate,self).get_context_data(**kwargs)
        context['name'] = 'Nikhil'
        return context

def hello_template_simple(request):
    name = 'Nikhil'
    return render_to_response('hello.html',{'name':name})

def index(request):
    html = "<html><body>Hello, Nikhil! It's a nice day, right? :)</body></html>"
    return HttpResponse(html)


def article(request,article_id):
    return render_to_response('article.html',{'article':Article.objects.get(id=article_id) })

def base(request):
    return render_to_response('base.html',{})

def extendedTemplate(request):
    return render_to_response('extended.html',{})


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html',{'articles':Article.objects.all(), 'language':language, 'session_language':session_language})

def language(request,language='en-gb'):
    response = HttpResponse("setting language to %s"%language)
    response.set_cookie('lang',language) #We use response here
    request.session['lang'] = language #We use request here
    return response

def create(request):
    if request.POST:
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html',args)

def like_article(request,article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/articles/get/%s'% article_id)
