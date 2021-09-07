from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta: #폼에 대한 정보 
        model= Article
        fields='__all__'
        #fields=['title','content'] #전부적는걸 권장함
        #fields=('title','content')
        #exclude=('title',) # 쉼표 매우중요 
        #exclude=>title빼고 
        #참고로 ('title') - 문자열이다 ('title')=='title' 튜플로 쓰려면 ,를찍어져야함