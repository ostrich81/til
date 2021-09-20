# 김서방 찾기

문제출처 - [코딩테스트 연습 - 서울에서 김서방 찾기 | 프로그래머스 (programmers.co.kr)](https://programmers.co.kr/learn/courses/30/lessons/12919)

문제 요약 

​	1. 김서방 찾기

input - 

```
seoul=["Jane", "Kim"]	
```

output-

```
return ="김서방은 1에 있다"

```

통과 코드 ...

```
def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            break
    answer =(f'김서방은 {i}에 있다')
    return answer
```

