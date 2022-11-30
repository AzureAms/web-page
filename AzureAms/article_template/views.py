from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Article, Core


def view_article(request):
    myarticles = Article.objects.all().values()
    #update order
    prev = 0
    for article in Article.objects.all():
        if article.order != prev+1:
            temp = article.order
            article.order = prev+1
            Article.objects.get(order=temp).delete()
        prev += 1
        article.save()
    #update order complete
    template = loader.get_template('view_article.html')
    context = {
    'myarticles': myarticles,
    }
    return HttpResponse(template.render(context, request))
  
def index(request):
    myarticles = Article.objects.all().values()
    #update order
    prev = 0
    for article in Article.objects.all():
        if article.order != prev+1:
            temp = article.order
            article.order = prev+1
            Article.objects.get(order=temp).delete()
        prev += 1
        article.save()
    #update order complete
    cores = Core.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'myarticles': myarticles[len(myarticles)-3:],
    'cores':cores,
    }
    return HttpResponse(template.render(context, request))

def article_page(request, order):
    template = loader.get_template('articleTemplate.html')
    article = Article.objects.get(order = order)
    context = {
        'article': article,
    }
    return HttpResponse(template.render(context, request))