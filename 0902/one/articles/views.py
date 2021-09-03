import articles
from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    # articles=Article.objects.all()[::-1] #파이썬이 변경 
    articles = Article.objects.order_by('-id') # 아이디 역순 정렬 orm으로 순서변경
    context={
        'articles':articles
    }
    return render(request,'articles/index.html',context)

def new(request):
    return render(request,'articles/new.html')

def create(request):
    print(request.POST)
    title=request.POST.get('title')
    content=request.POST.get('content')

    # article = Article()
    # article.title=title
    # article.content=content 
    # article.save()

    article=Article(title=title,content=content)
    #중간과정(Validation- 검증 )
    article.save()


    return redirect('articles:detail',article.pk)

def detail(request,pk):
    article= Article.objects.get(pk=pk)  # pk 첫번째는 db의 피케이고 둘째는 위에서 준 피케이다 
    context = {
        'article':article,
    }
    return render(request,'articles/detail.html',context)

def delete(request,pk):
    article =Article.objects.get(pk=pk) #삭제할 게시글 찾아오기 
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')

    else: 
        return redirect('articles:detail', article.pk)
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    context={
        'article':article,

    }
    return render(request,'articles/edit.html',context)

def update(request,pk):
    article=Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content= request.POST.get('content')
    article.save()

    return redirect('articles:detail',article.pk)