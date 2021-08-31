# 종이 붙이기

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

두 종류의 색종이가 있다.

1. 총 길이가 주어질때 두 종이를 써서 배치될 수 있는 경우의 수를 구하라 

   

input - 

```
3
30
50
70
```

output-

```
#1 5
#2 21
#3 85
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    a=int(input())
    if (a //10)%2 ==0:
        b=(a //10)
        answer=3
        if b==2:
            pass
        else:
            for i in range(3,b,2):
                answer+=2**i
    else:
        b = (a // 10)
        answer=1
        if b==1:
            pass
        else:
            for i in range(2,b,2):
                answer+=2**i

    print(f'#{t} {answer}')
```

