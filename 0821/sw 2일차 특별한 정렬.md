# 2일차 특별한 정렬

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 최대 최소 하나씩해서 10개만 출력하기

input - 

```
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26	 
```

output-

```
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    lsta=sorted(lst)
    answer=[]
    while len(lsta)!=0:
        answer.append(max(lsta))
        answer.append(min(lsta))
        lsta.remove(max(lsta))
        lsta.remove(min(lsta))
    ans=(answer[0:10])
    print(f'#{t}', end=' ')
    for i in (ans):
        print(i, end=" ")
    print()

```

