# list2 연습2

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AXO8W1vKRIwDFAXS&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210811_List2&problemBoxCnt=4&probBoxId=AXszJH26R3MDFAVy)

문제 요약 

 	1. 부분집합의 합이 0 이 되는지 안되는지

input - 

```
3
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
7 7 19 1 -18 5 -9 -11 19 18
 
```

output-

```
#1 0
#2 1
#3 1
```

해설코드 

```
def f(A):
    for i in range(1,1<<10):
        s=0
        for j in range(10):
            if i &(1<<j):
                s+=A[j]
                if s==0:
                    return 1
    return 0

T=int(input())
for t in range(1,T+1):
    arr = list(map(int,input().split()))
    print(f'#{t} {f(arr)}')
```

