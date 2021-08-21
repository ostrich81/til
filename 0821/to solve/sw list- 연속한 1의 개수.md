# 2일차 색칠하기

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 전기버스로 몇번에 갈수 있는지

input - 

```
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
```

output-

```
#1 3
#2 0
#3 4

```

해설코드 

```
T= int(input())
for t in range(1,T+1):
    K,N,M=list(map(int,input().split()))
    lst=list(map(int,input().split()))
    start=0
    after=0
    answer=-1
    while start<N:
        for i in range(start+K,start,-1):
            if i >=N or i in lst:
                after=i
                break
        if after==start:
            answer=0
            break
        else:
            answer+=1
            start=after
    print(f'#{t} {answer}')

```

