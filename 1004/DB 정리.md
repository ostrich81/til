1. 데이터 베이스로 얻는 장점들 

중복 최소화

무결성

일관성

독립성

표준화

보안 유지

2. sql 분류  // DMC 정의 조작 제어 

ddl - data definition language

ddl - create/ drop /alter = CDA 만들고 떨구고 바꾸고 

dml- data manipulation language

## dml - insert/select/update/delete = ISUD // 넣고 고르고 고치고 빼고 

dcl- data control language

dcl- grant/revoke/commit/rollback = grcr

3. 테이블 만들기 

```
CREATE TABLE classmates(
id INTEGER PRIMARY KEY , 
name TEXT
); 
```

 테이블 생성 확인 

```
.tables 
```

스키마 확인 

```
.schema classmates 
```

4. # 드랍 테이블 

```
DROP TABLE classmates; 
```

확인 

```
.tables 
```

하면 지워진거 확인할 수 있음 

5. 자료형 

-null

-integer

-real

-text

-blob 

6. # 인서트 넣는거 

```
INSERT INTO ......(ㅌ,ㅌ) VALUES (x,x);
```

```
INSERT INTO classmates(name,age) VALUES ('홍길동',23);
```

```
INSERT INTO classmates VALUES ('홍길동',23,'서울');
```

모든열에 데이터가 있으면 콜롬을 명시 안해줘도 됨 

다 넣고 내용 확인 

```
SELECT * FROM classmates; 
```

rowid는 자동 으로 입력됨 

```
SELECT rowid, * FROM classmates; 
```

7. where 

쿼리에서 반환된 행에 대한 특정 검색 조건을 지정 

```
SELECT rowid,name FROM classmates WHERE address='서울';
```

```
DELETE FROM classmates WHERE rowid=5;
```

재사용 방지 - 

id INTEGER PRIMARY KEY 뒤에 

 # AUTOINCREMENT 붙이기 

# 업데이트 셋 외우기 -- 아래 

```
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
```

```
SELECT * FROM users WHERE age >=30;
```

```
SELECT first_name FROM users WHERE age >=30;
```

```
SELECT age,last_name FROM users WHERE age >=30 AND last_name='김';
```

```
SELECT AVG(age) FROM users WHERE age>=30;
```

```
SELECT first_name, MAX(balance) FROM users;
```

```
SELECT AVG(balance) FROM users WHERE age>=30;
```

8. like 

# _ 랑 % :  자료 앞뒤로 몇글자나 있는지 없는지를 지칭

```
SELECT * FROM users WHERE age LIKE'2_';
```

```
SELECT * FROM users WHERE phone LIKE '02-%';
```

```
SELECT * FROM users WHERE first_name LIKE '%준';
```

```
SELECT * FROM users WHERE phone LIKE '%5114%';
```

9. order by

# asc 오름차순 / 기본

# desc 내림차순

```
SELECT * FROM users ORDER BY age ASC LIMIT 10;
```

```
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
```

```
SELECT * FROM last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```

10. # group by 에서 문장에 where 절이 포함되면 반드시 where 절 뒤에 작성해야 함 

```
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
```

as 를 활용해서 컬럼 명 변경 조회도 가능 

```
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
```

테이블 이름 바꾸기 

```
ALTER TABLE articles RENAME TO news;
```

칼럼 추가에서 문제 

```
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
- 이거하면 에러남
```

11. # 주관식 마지막 문제 에러가 나는 이유와 해결방안 

- 에러가 나는 이유 

테이블에 있던 기존 레코드 들에는 새로 추가할 필드에 대한 정보가 없다. 

따라서 넛 눌 형태의 컬럼은 추가가 불가능함 

- 해결방법 2가지 

넛눌 설정 없이 추가하기 

```
ALTER TABLE news ADD COLUMN created_at TEXT;
```

기본 값 설정하기 

```
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT ' 소제목';
```

12. 바꿔보세요 

-1

```
User.objects.all() 
```

```
SELECT * FROM users_user;
```

-2 #  중요

```
USER.objects.create(
first_name='길동',
last_nmae='홍',
age=100,
country='제주도',
phone ='010-1234-5678',
balance=10000
)
```

```
INSERT INTO users_user VALUES (102,'길동','김',100,'경상북도','010-1234-1234',100);
```

- 해당하는 항의 갯수 확인
- 이미 존재하는 아이디가 아닌지 확인 
- 넛눌값을 작성 했는지 확인 

-3  중요 !

```
User.objects.get(pk=102)
```

```
SELECT * FROM users_user WHERE id=102;
```

-4 

```
user= User.objects.get(pk=102)
user.last_name='김'
user.save()
user.last_name
```

```
UPDATE users_user SET first_name='철수' WHERE id=102;
SELECT * FROM users_user WHERE id=102;
```

-5 

```
User.objects.get(pk=102).delete()
```

```
DELETE FROM users_user WHERE id=101;
```

-6

```
User.objects.count()
```

```
SELECT COUNT(*) FROM users_user;
```

-7

```
User.objects.filter(age=30).values('first_name')
```

```
SELECT first_nmae FROM users_user WHERE age=30;
```

-8

gte개념 이상 greater than equal 

```
User.objects.filter(age__gte=30).count()
```

```
SELECT COUNT(*) FROM users_user WHERE age>=30;
```

-9

lte  lesser than equal

```
User.objects.filter(age__lte=20).count()
```

```
SELECT COUNT(*) FROM users_user WHERE age <=20;
```

-10

```
User.objects.filter(age=30,last_name='김').count()
```

```
User.objects.filter(age=30).filter(last_name='김').count()
```

```
SELECT COUNT(*) FROM users_user WHERE age=30 AND last_name='김';
```

-11

**Q 의 or 역활** 

```
from django.db.models import Q
User.objects.filter(Q(age=30) | Q(last_name='김'))
```

**Q 랑 | 를 기억할 것** 

```
SELECT * FROM users_user WHERE age=30 OR last_name='김';
```

-12

startswith

```
User.obejcts.filter(phone__startswith='02-').count()
```

```
SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
```

-13 중요 ! 

```
User.objects.filter(country='강원도',last_name='황').values('first_name')
```

```
SELECT first_name FROM users_user WHERE country='강원도' and last_name = '황';
```

-14 

# -를 넣어서 차순 바꾸는거 

```
User.objects.order_by('-age')[:10]
```

```
SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
```

-15 

```
User.objects.order_by('balance')[:10]
```

```
SELECT * FROM users_user ORDER BY balance ASC LIMIT 10;
```

-16 

```
User.objects.order_by('balance','-age')[:10]
```

```
SELECT * FROM users_user ORDER BY balance, age DESC LIMIT 10;
```

-17 중요! 

~번째 []

```
User.objects.order_by('-last_name','-first_name')[4]
```

```
SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
```

-18

```
from django.db.model import Avg
User.objects.aggregate(Avg('age'))
```

```
SELECT AVG(age) FROM users_user;
```

-19

```
from django.db.models import Avg
User.objects.filter(last_name='김').aggregate(Avg('age'))
```

```
SELECT AVG(age) FROM users_user WHERE last_name ='김';
```

-20

```
from django.db.models import Avg
User.objects.filter(country='강원도').aggreagte(Avg('balance'))
```

```
SELECT AVG(balance) FROM users_user WHERE country='강원도';
```

-21 중요!

```
from django.db.models import Max 
User.objects.aggregate(Max('balance'))
```

```
SELECT MAX(balance) FROM users_user;
```

-22

```
from django.db.models import Sum
User.objects.aggregate(Sum('balance'))
```

```
SELECT SUM(balance) FROM users_user;
```

Annotate- 주석 만들어내는 명령어 

23.

.tables 는 sql 문법이 아님 

24.

primary key 레코드의 고유값 pk - 유니크 조건 중요! + 넛눌 도 ! 

id 는 장고안에서만 쓰는 것 

데이터베이스에서는 pk 임 

25.  관계형 데이터베이스 

- 키와 값들의 간단한 관계를 표로 정리한 데이터베이스 

26.

limit - offset 키워드와 함께 사용 하는 거 

5번째는 offset 4

select distinct 중복제거 하는거 

27.

삭제는 REMOVE 가 아님 

무조건 DELETE 임 

28.

Count/ Avg / Max/ Min / SUM 중에 나옴 

29.

겟/ 카운트/ 필터/오더바이/ 어그리게이트

