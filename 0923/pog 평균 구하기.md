# pro

문제출처 - [[코딩테스트 연습 - 평균 구하기 | 프로그래머스 (programmers.co.kr)](https://programmers.co.kr/learn/courses/30/lessons/12944)

문제 요약 

​	1. 평균

input - 

```
arr=[1,2,3,4]	
```

output-

```
2.5
```

해설코드 

```
def solution(arr):
    a=(sum(arr))
    b=(len(arr))
    answer = a/b
    return answer
```

