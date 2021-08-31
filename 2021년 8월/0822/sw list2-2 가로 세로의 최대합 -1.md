# list 가로 세로의 최대합

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXYELfqa6pYDFAST&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210812_List2실습&problemBoxCnt=10&probBoxId=AXs3nF-6yrADFARW)

문제 요약 

 	1. 한 칸에 해당하는 가로세로합의 최대값

input - 

```
3
4
1 2 0 1
2 1 0 1
1 2 3 2
3 2 2 3
4
3 2 3 0
0 2 2 0
2 3 2 2
2 1 2 1
5
2 4 3 1 3
4 0 2 3 2
2 0 3 4 3
1 3 4 3 1
3 0 3 3 4

```

output-

```
#1 15
#2 16
#3 26
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst=[]
    for i in range(n):
        inpu=list(map(int,input().split()))
        lst.append(inpu)
    answer=0
    for i in range(n):
        for j in range(n):
            total=(sum(lst[i])-lst[i][j])
            for k in range(n):
                total+=lst[k][j]
            answer=max(answer,total)
    print(f'#{t} {answer}')
```

