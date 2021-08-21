# 자기 방으로 돌아가기

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AWNcJ2sapZMDFAV8&probBoxId=AXtSam9qcc0DFARW&type=PROBLEM&problemBoxTitle=20210820_문제풀이1&problemBoxCnt=8)

문제 요약 

 	1. 겹치면 한단위시간씩 써서 방으로 돌아갈때 총걸리는 시간 

input - 

```

3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
2 200
3
10 100
20 80
30 50	// T : 테스트케이스 수
// N : 돌아가야 할 학생들의 수
// 10 : 현재 방, 20 : 돌아갈 방



// 두번째 테스트케이스의 N





 
```

output-

```

#1 1
#2 2
#3 3	// Test Case 1의 정답
// Test Case 2의 정답
// Test Case 3의 정답
```

해설코드 

```
def div(num):
    return(int(num)+1)//2

T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst =[list(map(div,input().split())) for _ in range (n) ]
    z=[0]*201
    for i in range(n):
        if lst[i][0]>lst[i][1]:
            lst[i][0],lst[i][1]=lst[i][1],lst[i][0]
        for j in range(lst[i][0],lst[i][1]+1):
            z[j]+=1
        answer=max(z)
    print(f'#{t} {answer}')


```

