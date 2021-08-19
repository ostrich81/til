# 파스칼 삼각형 

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq&categoryId=AV5P0-h6Ak4DFAUq&categoryType=CODE&problemTitle=2005&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)

문제 요약 

크기가 N 인 파스칼 삼각형을 만들어야 한다. 

1. 첫번째 줄은 항상 숫자 1이다 
2. 두번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 숫자의 합으로 구성된다.

input - 

```
1
4
 
```

output-

```
#1
1
1 1
1 2 1
1 3 3 1
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    a=int(input())
    lst=[[1] * x for x in range(1,a+1)]
    for i in range(1,a-1):
        for j in range(len(lst[i])-1):
            lst[i+1][j+1]=lst[i][j] + lst[i][j+1]

    print(f'#{t}')
    for k in lst:
        print(*k)

```

