# 백만 장자 프로젝트

문제출처 -[SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV5LrsUaDxcDFAXc&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210820_문제풀이1&problemBoxCnt=8&probBoxId=AXtSam9qcc0DFARW)

문제 요약 

 	1. 매매가가 높은 날만 팔아치우기

input - 

```
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
```

output-

```
#1 0
#2 10
#3 5
```

제출코드 

```
T=int(input())
for t in range(1,T+1):
    a=int(input())
    lst=list(map(int,input().split()))
    b=len(lst)
    j=0
    answer = 0
    c = []
    while j<b-1:
        # print(j)
        # print(b-1)
        if lst[j]>lst[j+1]:
            answer+=len(c)*lst[j]-sum(c)
            c = []
            j+=1
            if j ==b-1:
                answer += (len(c) * lst[j]) - sum(c)
                c = []
            else:
                pass

        elif lst[j]<=lst[j+1]:
            c.append(lst[j])
            j+=1
            if j ==b-1:
                answer += (len(c) * lst[j]) - sum(c)
                c = []
            else:
                pass
    print(f'#{t} {answer}')

```



해설코드 

```
T = int(input())
for t in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    last = arr[-1]
    cnt = 0
    for i in range(len(arr)-1,-1,-1): # 핵심! 뒤부터 보기
        if last > arr[i]:
            cnt += last-arr[i]
        else: # 같거나 작을 때 
            last = arr[i]
    print("#{} {}".format(t, cnt))
```

한줄 ... 반례가 뭐지 테스트 케이스는 다되는데 ...... 하 
