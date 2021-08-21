# 쇠막대기 자르기

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AWVl47b6DGMDFAXm&probBoxId=AXtSam9qcc0DFARW&type=PROBLEM&problemBoxTitle=20210820_문제풀이1&problemBoxCnt=8)

문제 요약 

 	1. 쇠막대기와 레이저를 지나 잘려진 조각의 총 개수 확인

input - 

```

2
()(((()())(())()))(())
(((()(()()))(())()))(()())	//전체 TC 개수
//첫 번째 TC
//두 번째 TC
```

output-

```

#1 17
#2 24	//첫 번째 TC의 출력
//두 번째 TC의 출력
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    board = list(input())
    now=0
    cut=0
    a=0
    while True :
        if board[now]=='(':
            if board[now+1]==')':
                now+=2
                cut+=a
            else:
                now+=1
                a+=1
        else:
            now+=1
            cut+=1
            a-=1
        if now ==len(board):
            break
    print(f'#{t} {cut}')
```

