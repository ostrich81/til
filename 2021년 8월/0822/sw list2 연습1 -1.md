# list2 연습 1 

문제출처 -[SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AXO8PeFqQsUDFAXS&probBoxId=AXszJH26R3MDFAVy&type=USER&problemBoxTitle=20210811_List2&problemBoxCnt=4)

문제 요약 

 	1. 근접 요소들의 합 구하기

input - 

```
3
5
45 15 10 56 23 
96 98 99 40 69 
96 84 49 46 34 
16 64 81 4 11 
10 66 85 55 14 
5
44 91 64 73 62 
78 72 52 73 48 
44 88 55 75 24 
22 72 59 26 62 
87 11 64 79 40 
5
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
10 10 10 10 10
```

output-

```
#1 2430
#2 2244
#3 0
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    N=int(input())
    lst=[list(map(int,input().split())) for _ in range(N)]
    answer=0
    for i in range(N):
        for j in range(N):
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni,nj=i+di,j+dj
                if 0<=ni<N and 0<=nj<N:
                    answer += abs(lst[i][j]-lst[ni][nj])
    print(f'#{t} {answer}')

```

