# 수 정렬하기

문제출처 - [[2750번: 수 정렬하기 (acmicpc.net)](https://www.acmicpc.net/problem/2750)

문제 요약 

​	1. 주어진 수에 대해 정렬

input - 

```
5
5
2
3
4
1
```

output-

```
1
2
3
4
5
```

해설코드 

```
T=int(input())
a= (int(input()) for _ in range(1,T+1))
k=(list(a))
l=sorted(k)
for i in range(len(l)):
    print(l[i])
```

