# 3일차 문자열 비교

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 안에 포함 되어 있는지

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
#1 1
#2 0
#3 1
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    a=(input())
    b=input()
    if a in b:
        answer=1
    else:
        answer=0
    print(f'#{t} {answer}')
```

