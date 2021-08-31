# list 당근 수확

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AW2ZiPcaPQ8DFAWg&probBoxId=AXstUdj67bMDFARW&type=USER&problemBoxTitle=20210809_List1실습&problemBoxCnt=11)

문제 요약 

 	1. 두 명의 당근 수확량이 가장 적게 차이나는 분할점 찾기

input - 

```
3
5
10 8 7 4 9
10
9 4 1 6 9 10 0 5 8 2
10
3 1 6 8 0 9 7 9 9 7

```

output-

```
#1 2 2
#2 5 4
#3 6 5

```

해설코드 

```
T= int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    A=[]
    B=[]
    for i in range(len(lst)):
        a=sum(lst[:i])
        b=sum(lst)-a
        A.append(i)

        if (b-a)<0:
            c=(b-a)*-1
        else:
            c=b-a
        B.append(c)
    z=B.index(min(B))
    x=min(B)
    print(f'#{t} {z} {x}')

```

