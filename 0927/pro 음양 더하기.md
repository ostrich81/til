# pro 음양 더하기

문제출처 - [코딩테스트 연습 - 음양 더하기 | 프로그래머스 (programmers.co.kr)](https://programmers.co.kr/learn/courses/30/lessons/76501)

문제 요약 

​	1. 음양 숫자 더하기

input - 

```
absolutes	signs	result
[4,7,12]	[true,false,true]	
[1,2,3]	[false,false,true]	
```

output-

```
result 9 / 0 
```

해설코드 

```

def solution(absolutes, signs):
    answer=0
    for i in range(len(absolutes)):
        # print(signs[i])
        # print(absolutes[i])
        if signs[i]==True:
            answer+=absolutes[i]
            # print(answer)
        elif signs[i]==False:
            answer-=absolutes[i]
            # print(answer)
    return answer
```



파이썬 안쓰고 .. 대문자랑 소문자랑 문자열이랑 제대로 안주네 여기 .. 
