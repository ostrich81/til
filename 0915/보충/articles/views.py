from django.shortcuts import get_object_or_404, redirect, render
from articles.forms import ArticleForm
from .models import Article
# Create your views here.
def create(request):
    if request.method=="POST":
        form =ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form =ArticleForm()
    context={
        'form':form,
        }
    return render(request, 'articles/form.html',context)

def index(request):
    # articles= Article.objects.all()
    articles= Article.objects.order_by('-pk')
    context  = {
            'articles': articles,

    }
    return render(request,'articles/index.html',context)

def detail(request,pk):
    # article=Article.objects.get(pk=pk)
    article=get_object_or_404(Article,pk=pk)
    context={
        'article':article,
    }
    return render(request,'articles/detail.html',context)

def delete(request,pk):
    article=Article.objects.get(pk=pk)
    if request.method =='POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail',article.pk)

def update(request,pk):
    article=Article.objects.get(pk=pk)
    if request.method=="POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article=form.save()
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(instance=article)
    context={
        'form':form,
        'article':article,
    }
    return render(request,'articles/form.html',context)