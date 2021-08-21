# 1일차 min max

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 최대에서 최소빼기

input - 

```
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
```

output-

```
#1 630739
#2 740510
#3 838110
```

해설코드 

```
T= int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    a=max(lst)-min(lst)
    print(f'#{t} {a}')
```

