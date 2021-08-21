# 2일차 색칠하기

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 색칠해서 중복된 칸 수 제출

input - 

```
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
```

output-

```
#1 4
#2 5
#3 7
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    base=[[0]*10 for _ in range(10)]
    answer=0
    for i in range(n):
        a1,a2,b1,b2,c=list(map(int,input().split()))

        for i in range(a1,b1+1):
            for j in range(a2,b2+1):
                if base[i][j]==1:
                    answer+=1
                elif base[i][j]==0:
                    base[i][j]+=1

    print(f'#{t} {answer}')

```

