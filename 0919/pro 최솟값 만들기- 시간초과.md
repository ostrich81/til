# 최솟값 만들기 

문제출처 - [코딩테스트 연습 - 최솟값 만들기 | 프로그래머스 (programmers.co.kr)](https://programmers.co.kr/learn/courses/30/lessons/12941)

문제 요약 

​	1. 최솟값 만들기

input - 

```
A=[1,4,2]
B=[5,4,4]
```

output-

```
answer=29
```

시간초과 코드 ...

```
from itertools import permutations
def solution(A,B):
    pa=(list(permutations(A)))
    pb=(list(permutations(B)))
    # print(pa)
    # print(pb)
    lista=[]
    answer = 0
    for a in range(len(pa)):
        for b in range(len(pb)):
            answer=0
            K=pa[a]
            P=pb[b]
            for i in range(len(A)):
                answer=answer+(K[i]*P[i])
            lista.append(answer)
    answer=min(lista)        

    return answer
```

