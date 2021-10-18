rdbms 관계형 데이터베이스 

참조 무결성 

- 데이터 베이스 관계모듈에서 2개의 테이블 간의 일관성 
- 모든 댓글은 어떠한 게시글에 속해있는 것을 지칭 
- 지은이가 없는 게시글은 없는 것 

프라이머리키 - 유일무이한 것 primary

포린키 - 그 안에 속해 있는 것들 foreign

1. 참조하는 모델 클래스 
2. 온 딜리트 옵션 - 메인이 죽으면 속해있는 것들 다 죽이는 것 

> 캐스케이드 밖에  안씀 사실 )) 

CASCADE 

항상 단수로 지정하는 것이 좋음 >>아티클 >

article = models.ForeignKey(Article, on_delete=models.CASCADE)

[django/models.py at 569a33579c3cca5f801c544d9b52a34e3c779424 · django/django · GitHub](https://github.com/django/django/blob/569a33579c3cca5f801c544d9b52a34e3c779424/django/contrib/auth/models.py#L321)

[django/base_user.py at 569a33579c3cca5f801c544d9b52a34e3c779424 · django/django · GitHub](https://github.com/django/django/blob/569a33579c3cca5f801c544d9b52a34e3c779424/django/contrib/auth/base_user.py#L47)

커스텀 유저모델 수동으로 찾아와서 하는 방식 있긴한데 안씀 

겟유저 모델을 써라 ... 

--

