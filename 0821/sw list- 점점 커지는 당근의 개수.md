# list 점점 커지는 당근의 개수

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AW_nY2m6OLADFARY&probBoxId=AXstUdj67bMDFARW&type=USER&problemBoxTitle=20210809_List1실습&problemBoxCnt=11)

문제 요약 

 	1. 연속된 큼의 몇번까지 인지 세기

input - 

```
3
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
```

output-

```
#1 5
#2 3
#3 1
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    lsta=lst+[0]
    i=0
    g=[]
    answer=1
    while i<n:
        if lsta[i] <lsta[i+1]:
            answer+=1
            i+=1
        elif lsta[i] >=lsta[i+1]:
            i+=1
            g.append(answer)
            answer=1
    print(f'#{t} {max(g)}')

```

