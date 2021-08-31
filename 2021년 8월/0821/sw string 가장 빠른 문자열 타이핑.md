# string 가장 빠른 문자열 타이핑

문제출처 -[SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AV_65wkqsb4DFAWS&probBoxId=AXtRpR-qVrADFARW&type=PROBLEM&problemBoxTitle=20210817_String실습&problemBoxCnt=5)

문제 요약 

 	1. 문자열을 치환하면 몇번 타이핑 해야하는지

input - 

```

2
banana bana
asakusa sa	//Test Case의 개수
//A=”banana”, B=”bana”
//A=”asakusa”, B=”sa”
```

output-

```
#1 3
#2 5	//Test Case 1번의 답
//Test Case 2번의 답
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    lst=list(map(str,input().split()))
    a=lst[0]
    ta=len(a)
    b=lst[1]
    tb=len(b)
    if b in a:
        time=a.count(b)
    answer=ta-(tb*time)+time
    print(f'#{t} {answer}')


```

