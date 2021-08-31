# 알람시계

문제출처 - [2884번: 알람 시계 (acmicpc.net)](https://www.acmicpc.net/problem/2884)

문제 요약 

​	1. 알람시계 45분 땡기기

input - 

```
10 10
```

output-

```
9 25
```

해설코드 

```
h, m=list(map(int,input().split()))
realm=0
realh=0
if m >=45:
    realh=h
    realm=m-45
else:
    if h==0:
        realh=23
        realm=m+15
    else:
        realh=h-1
        realm = m  +15
print(realh, realm)
```

