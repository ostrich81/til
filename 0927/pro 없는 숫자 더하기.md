# pro 없는 숫자 더하기

문제출처 - [코딩테스트 연습 - 없는 숫자 더하기 | 프로그래머스 (programmers.co.kr)](https://programmers.co.kr/learn/courses/30/lessons/86051)

문제 요약 

​	1. 일의자리 없는 숫자 더하기

input - 

```
numbers=[1,2,3,4,6,7,8,0]	
```

output-

```
14
```

해설코드 

```
def solution(numbers):
    a=[0,1,2,3,4,5,6,7,8,9]
    for i in (numbers):
        if i in a:
            a.remove(i)
    print(a)
    answer = sum(a)
    return answer
```

