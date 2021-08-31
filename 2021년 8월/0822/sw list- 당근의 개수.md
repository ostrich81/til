# list 당근의 개수

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AW_nQxnaNUgDFARY&probBoxId=AXstUdj67bMDFARW&type=USER&problemBoxTitle=20210809_List1실습&problemBoxCnt=11)

문제 요약 

 	1. 당근이 가장 많은 텃밭과 갯수

input - 

```
3
5
948 313 785 388 930 
10
145 642 753 157 660 415 625 718 310 481 
20
379 644 716 21 608 819 321 391 227 58 294 687 764 295 412 540 494 10 414 942 
```

output-

```
#1 1 948
#2 3 753
#3 20 942
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))
    print(f'#{t} {lst.index(max(lst))+1} {max(lst)}')
```

