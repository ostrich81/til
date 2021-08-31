# list 당근 수확2

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AW2cNnEqS8EDFAWg&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210809_List1실습&problemBoxCnt=11&probBoxId=AXstUdj67bMDFARW)

문제 요약 

 	1. 당근 총 수확하는 총 거리 

input - 

```
3
5 6
10 8 7 4 9
10 100
9 4 1 6 9 10 0 5 8 2
10 6
3 1 6 8 0 9 7 9 9 7
```

output-

```
#1 46
#2 20
#3 138
 
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    N,M=list(map(int,input().split()))
    lst=list(map(int,input().split()))
    answer=0
    i=0
    cap=M
    while True:
        if lst[i]>=cap:
            answer +=2*(i+1)
            lst[i]-=cap
            cap=M
        else:
            cap-=lst[i]
            i+=1
            if i ==N:
                answer +=2*i
                break
    print(f'#{t} {answer}')

```

