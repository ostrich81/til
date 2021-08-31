# 삼성시의 버스노선

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AWczm7QaACgDFAWn&probBoxId=AXtSam9qcc0DFARW&type=PROBLEM&problemBoxTitle=20210820_문제풀이1&problemBoxCnt=8)

문제 요약 

 	1. 5000 개의 버스노선중 각 노선별 몇 버스가 지나는지 구하기

input - 

```

1
2
1 3
2 5
5
1
2
3
4
5	//테스트 케이스 개수
//첫 번째 테스트 케이스, N=2
// A1 = 1, B1 = 3
// A2 = 2, B2 = 5
// P = 5
// 이하 C1 = 1, C2 = 2, C3 = 3, C4 = 4, C5 = 5



 
```

output-

```

#1 1 2 2 1 1	//첫 번째 테스트 케이스 결과
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n= int(input())
    # print(n)
    lst=[0]*5000
    # print(lst)
    # B=[]
    for _ in range(n):
        a,b=list(map(int,input().split()))
        # B+=[b]
        # print(a,b)
        while b>=a:
            # if b>a:
                lst[a-1]+=1
                a+=1
        # print(lst)
    # s=max(B)
    c=int(input())
    answer=[]

    for _ in range(c):
        g=int(input())
        answer+=[lst[g-1]]

    print(f'#{t}', end=" ")
    for i in (answer):
        print(i, end=" ")
    print()


```

한줄 ... 

c 번 은 그냥 p까지의 그게 아니라 몇개 해당하는 정류장을 말하는거다.... 
