# list 연속한 1의 개수

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AXALDUIq97oDFASI&probBoxId=AXstUdj67bMDFARW&type=USER&problemBoxTitle=20210809_List1실습&problemBoxCnt=11)

문제 요약 

 	1. 1이 연속해서 나오는 개수

input - 

```
3
10
0011001110
10
0000100001
10
0111001111
```

output-

```
#1 3
#2 1
#3 4
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    answer=0
    lst=list(map(int,input()))
    lsta=lst+[0]
    # print(lsta)
    g=[]
    i=0
    while i<n+1:
        if lsta[i]==1:
            answer+=1
            i+=1
        else:
            g.append(answer)
            answer=0
            i+=1
    print(f'#{t} {max(g)}')
```

