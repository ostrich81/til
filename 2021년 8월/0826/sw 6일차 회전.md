# sw 6일차 회전

문제출처 -[[SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 돌고 돌린 숫자

input - 

```
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907	 
```

output-

```
#1 731
#2 18641
#3 2412
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    N,M=list(map(int,input().split()))
    lst=list(map(int,input().split()))
    for i in range(M):
        stack=[]
        stack.append(lst[0])
        lst=lst[1:]+stack
    print(f'#{t} {lst[0]}')

```



