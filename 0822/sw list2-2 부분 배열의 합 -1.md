# 부분 배열의 합 

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AXX1zqK6qIwDFAST&probBoxId=AXs3nF-6yrADFARW&type=USER&problemBoxTitle=20210812_List2실습&problemBoxCnt=10)

문제 요약 

 	1. 전기버스로 몇번에 갈수 있는지

input - 

```
3
5 3 3
0 1 1 0 1 
1 1 0 1 1 
0 1 1 0 0 
0 0 1 0 0 
1 0 1 0 0 
10 8 6
0 1 1 1 1 0 0 0 1 1 
1 1 1 1 1 0 1 0 1 1 
1 1 0 1 0 1 0 1 1 0 
1 0 0 1 1 1 0 1 0 1 
0 1 1 0 0 1 0 0 0 0 
1 1 1 0 1 1 0 1 0 1 
0 0 1 1 1 1 1 0 0 0 
1 1 0 0 1 0 1 0 1 1 
1 1 0 0 1 0 1 0 1 1 
1 1 0 1 0 0 1 1 0 0 
20 12 16
1 0 0 0 0 1 1 0 1 0 0 0 0 1 1 1 0 1 1 1 
0 0 0 0 1 1 0 1 1 1 0 1 1 0 1 1 0 0 0 0 
1 1 1 1 0 1 1 1 0 0 0 0 0 0 0 1 1 0 0 1 
0 0 1 1 1 1 0 0 0 0 1 0 0 1 1 0 1 1 1 1 
1 1 0 0 1 0 0 0 1 0 1 1 0 0 1 1 0 1 1 1 
0 1 0 0 0 1 1 0 1 0 1 1 1 1 0 0 1 0 0 0 
0 0 0 1 0 0 1 1 1 0 1 0 0 1 1 1 0 1 1 1 
0 0 1 1 1 1 0 0 0 1 0 1 1 0 1 1 1 0 1 0 
1 1 0 1 0 1 0 0 0 0 0 1 1 1 0 0 1 1 1 0 
1 0 0 1 1 1 1 1 0 0 0 0 1 1 0 0 1 0 1 1 
0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 1 
0 0 0 1 0 1 1 0 1 1 0 0 1 0 1 1 0 0 1 1 
1 1 1 1 1 1 0 1 1 1 1 1 0 0 1 0 1 1 1 0 
1 0 0 1 0 1 1 0 0 1 1 0 1 0 0 0 0 0 0 0 
0 1 1 1 0 0 1 1 1 1 0 1 0 0 1 0 1 1 0 1 
1 0 0 0 1 0 0 1 0 1 1 0 0 1 0 0 1 0 0 1 
0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 0 0 
1 1 1 1 1 1 1 1 1 0 0 0 1 1 1 0 1 0 0 0 
0 1 0 1 0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 1 
1 0 1 0 1 0 0 1 1 1 1 0 1 0 0 1 0 1 0 1

```

output-

```
#1 6
#2 32
#3 104
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    N,n,m=list(map(int,input().split()))
    lst=[]
    for i in range(N):
        a=list(map(int,input().split()))
        lst.append(a)
    answer=0
    for i in range(N-n+1):
        for j in range(N-m+1):
            b=0
            for z in range(n):
                for x in range(m):
                    b +=lst[i+z][j+x]
            answer=max(answer,b)
    print(f'#{t} {answer}')
```

