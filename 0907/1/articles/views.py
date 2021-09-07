from django.shortcuts import redirect, render
from .models import Article 
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles=Article.objects.all()

    context={
        'articles':articles,
    }
    return render(request,'articles/index.html',context)

def create(request):
    #5. 크리에이트 경로로 요청이 들어옴(포스트)잘못된 케이스1.->잘못된 입력 >사용자가 데이터 입력 
    #10. 크리에이트 경로로 요청이 들어옴(포스트)올바른 입력2. ->사용자가 데이터 입력
    if request.method=='POST':
        # 6. 데이터가 입력된 종이를 가져옴 ->아티클폼을 인스턴스화 (사용자 데이터 받아서)
        #빈종이와 사용자 데이터 합침 
        #11.데이터가 입력된 종이를 가져옴 ->아티클폼을 인스턴스화 (사용자 데이터 받아서)
        #빈종이와 사용자 데이터 합침 
        form=ArticleForm(data=request.POST) # data= 생략가능
        #7. 사용자가 입력한 데이터가 유효한지 올바른지 확인 
        #12.사용자가 입력한 데이터가 유효한지 올바른지 확인 
        if form.is_valid():
            # 13. 올바른 데이터이면 데이터를 디비에 저장한다. 
            form.save()
            #14. 인덱스로 리다이렉트 시켜준다. 
            return redirect('articles:index')
    #1. create경로로 요청이 들어옴-겟 
    else: #겟요청 -디비에 영향x- 빈 종이(폼) 응답 
        form=ArticleForm() #2. 아티클폼을 인스턴스화 한다> 빈종이 생성 

    context={ #3. 사용자에게 빈종이를 주기 위해서 컨텍스트에 폼을 담는다. 
    #8. 잘못된 데이터를 다시 입력 받기위해서 컨텍스트에 폼을 담는다.
        'form':form,
    }
    #4. 사용자에게 데이터를 받기 위해 빈 종이를 넘겨준다.>데이터를 입력한다.
    #9. 사용자에게 올바른 데이터를 받기 위해 폼을 넘겨준다. 
    return render(request,'articles/create.html',context)

def detail(request,pk):
    article=Article.objects.get(pk=pk)
    context={
        'article':article,

    }
    return render(request,'articles/detail.html',context)

def delete(request,pk):
    article=Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request,pk):
    article=Article.objects.get(pk=pk)
    if request.method=='POST':
        form=ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article=form.save() #article에 수정 완료된 1줄이들어감 
            return redirect('articles:detail',article.pk)
    else: #get요청
        form=ArticleForm(instance=article) #기존의 내용을 담아서 보냄 
    context={
        'article':article, #아티클스.피케이를 에이테그로 사용하려고 
        'form':form,
    }
    return render(request,'articles/update.html',context)