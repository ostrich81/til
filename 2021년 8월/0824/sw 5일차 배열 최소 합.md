# sw 5일차 배열 최소 합

문제출처 -[SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemSubmitDetail.do)

문제 요약 

 	1. 각 줄에서 안겹치게 뽑아서 최소 합구하기

input - 

```
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
```

output-

```
#1 8
#2 14
#3 9
```

해설코드 

```
def f (i,N,s):
    global mins
    if i ==N:
        if mins>s:
            mins=s
    elif mins <=s:
        return
    else:
        for j in range(i,N):
            p[i],p[j]=p[j],p[i]
            f(i+1,N,s+lst[i][p[i]])
            p[i],p[j]=p[j],p[i]
        return
T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]
    mins=10*N*N
    p=list(range(N))
    f(0,N,0)
    print(f'#{t} {mins}')
```



이건 모르겠다 ...
