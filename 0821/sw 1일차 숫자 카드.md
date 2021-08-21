# 1일차 숫자 카드

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 가장 많이 나온 숫자카드와 갯수

input - 

```
3
5
49679
5
08271
10
7797946543
```

output-

```
#1 9 2
#2 8 1
#3 7 3
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    k=[0]*10
    lst=list(((input())))
    for i in range(len(lst)):
        a=lst[i]
        A=int(a)
        k[A]+=1
    time=max(k)
    card = []
    if k.count(time)>1:
        for i in range(len(k)):
            if k[i]==time:
                card+=[i]
                answer=max(card)
    else:
        answer=k.index(time)
    print(f'#{t} {answer} {time}')

```

