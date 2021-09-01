from django.db import models

# Create your models here.
class Article(models.Model):
    #id
    #id = models.AutoField(primart_key=True)1,2,3,4,

    title = models.CharField(max_length=10)  # max_length 가 필수 ! -> 위젯 ! 에서 차이남  # 작은칸 제목칸 둘다 텍스트필드도 상관없음
    content= models.TextField() # max_length 가 옵션 # 큰칸 내용칸 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)