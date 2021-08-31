# 1일차 구간합

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 구간별 최대값과 최소값 차이 출력

input - 

```
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
```

output-

```
#1 21
#2 11088
#3 1090
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    N,M=list(map(int,input().split()))
    lst=list(map(int,input().split()))
    lsta=[]
    for i in range(N-M+1):
        lsta+=[sum(lst[i:i+M])]
    answer=(max(lsta)-min(lsta))
    print(f'#{t} {answer}')
```

