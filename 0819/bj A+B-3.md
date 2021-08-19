# A+B-3

문제출처 - [10950번: A+B - 3 (acmicpc.net)](https://www.acmicpc.net/problem/10950)

문제 요약 

​	1. 그냥더하는건데?

input - 

```
5
1 1
2 3
3 4
9 8
5 2
```

output-

```
2
5
7
17
7
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    a,b=list(map(int,input().split()))
    print(a+b)
```

