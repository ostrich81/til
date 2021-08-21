# 3일차 글자수

문제출처 -[SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 안에 포함된 글자 수 중 큰 것

input - 

```

3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
```

output-

```
#1 2
#2 1
#3 3
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    lista=list(map(str,input()))
    listb=list(map(str,input()))
    ans=[]
    for i in lista:
        if i in listb:
            ans.append(listb.count(i))
    answer=max(ans)
    print(f'#{t} {answer}')
```

