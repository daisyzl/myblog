from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    articles = models.Article.objects.all()#集合列表
    return render(request,'index.html',{'articles':articles})#http://127.0.0.1:8000/blog/
    # article = models.Article.objects.get(pk=1)
    # return render(request,'index.html',{'article':article})#http://127.0.0.1:8000/blog/
    # return render(request,'index.html',{'hello':'hello,blog!'})  #http://127.0.0.1:8000/blog/
    # return HttpResponse("Hello World!")

def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article':article})

def edit_page(request):
    return render(request,'edit_page.html')

# Create your views here.
