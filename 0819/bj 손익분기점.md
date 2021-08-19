# 손익 분기점

문제출처 - [1712번: 손익분기점 (acmicpc.net)](https://www.acmicpc.net/problem/1712)

문제 요약 

​	1. 노트북을 생산하는데 총 비용 두가지를 합쳐서 총 수입이 비용보다 많아지는 시점 계산

input - 

```
1000 70 170

```

output-

```
11
```

해설코드 

```
a,b,c =list(map(int,input().split()))
# print(a,b,c)
if b>= c:
    print(-1)
else:
    sud=c-b
    answer=(a//sud)+1
    print(answer)
```

