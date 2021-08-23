# 당근밭 옆 고구마밭

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AW323bY6_iwDFAWg&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210809_List1실습&problemBoxCnt=11&probBoxId=AXstUdj67bMDFARW)

문제 요약 

 	1. 가장 긴 뿌리의 고구마 개수

input - 

```
4
8
1 2 3 4 5 1 2 3
7
1 2 3 4 3 2 1
9
1 2 3 2 3 4 1 2 3
5
1 9 1 2 3
```

output-

```
#1 2 15
#2 1 10
#3 3 9
#4 2 6
```

제출코드

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    lsta=lst+[0]
    leng=[]
    l=0
    cnt=[]
    c=0
    answer=0
    for i in range(len(lsta)-1):
        if lsta[i]<lsta[i+1]:
            l+=1
            c+=lsta[i]
        else:
            l+=1
            leng.append(l)
            l=0
            c += lsta[i]
            cnt.append(c)
            c=0
    for i in range (len(leng)):
        if leng[i]>1:
            answer+=1
    m=max(leng)
    M=[]
    if leng.count(m)>1:
        for i in range(len(leng)):
            if leng[i]==m:
                M.append(cnt[i])
                p=max(M)
    else:
        p=cnt[leng.index(max(leng))]

    print(f'#{t} {answer} {p}')

```



해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    lsta=lst+[0]
    leng=[]
    l=0
    cnt=[]
    c=0
    answer=0
    for i in range(len(lsta)-1):
        if lsta[i]<lsta[i+1]:
            l+=1
            c+=lsta[i]
        else:
            l+=1
            leng.append(l)
            l=0
            c += lsta[i]
            cnt.append(c)
            c=0
    for i in range (len(leng)):
        if leng[i]>1:
            answer+=1
    m=max(leng)
    M=[]
    if leng.count(m)>1:
        for i in range(len(leng)):
            if leng[i]==m:
                M.append(cnt[i])
                p=max(M)
    else:
        p=cnt[leng.index(max(leng))]
    if max(leng)==1:
        print(f'#{t} {0} {0}')
    else:
        print(f'#{t} {answer} {p}')

```

테케 10개중9개 6개중 5개 맞는게 제일 하 ....... 미치겟다 그런게 

고쳤다. 0 일경우에 1인거 찾았다... 
