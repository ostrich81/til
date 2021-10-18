python -m venv venv

$ pip install -r requirements.txt

아티클스 모델스 피와이 

```
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
```

하고마이그레이트 

$ python manage.py makemigrations

1 

1

$ python manage.py migrate

$ python manage.py runserver

폼스 피와이 

```
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = {'title','content'}

```

뷰즈 피와이

```
  article = form.save(commit=False)
            article.user=request.user
```

인덱스 

```
  {% for article in articles %}
  <p><b>작성자 : {{article.user}}</b></p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
```

