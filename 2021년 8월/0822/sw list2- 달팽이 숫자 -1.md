# 달팽이 숫자

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV5PobmqAPoDFAUq&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210811_List2&problemBoxCnt=4&probBoxId=AXszJH26R3MDFAVy)

문제 요약 

 	1. 달팽이 숫자 표현

input - 

```
2    
3   
4    
```

output-

```
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
 
```

해설코드 

```
T=int(input())

for t in range(1,T+1):
    N=int(input())
    lst=[[0 for _ in range(N)] for _ in range(N)]
    num=1
    row=0
    col=-1
    trans=1
    while N>0:
        for _ in range(N):
            col+= trans
            lst[row][col]=num
            num+=1
        N-=1
        for _ in range(N):
            row += trans
            lst[row][col]=num
            num +=1
        trans *= -1
    print(f'#{t}')
    for i in range(len(lst)):
        print(*lst[i])
```

