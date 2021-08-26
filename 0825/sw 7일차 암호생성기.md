# sw 7일차 암호생성기

문제출처 [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AV14uWl6AF0CFAYD&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210825_Queue&problemBoxCnt=2&probBoxId=AXt8Tk_Ko3kDFAVy)

문제 요약 

 	1. 계산기

input - 

```
1
9550 9556 9550 9553 9558 9551 9551 9551 
2
2419 2418 2423 2415 2422 2419 2420 2415 
3
7834 7840 7840 7835 7841 7835 7835 7838 
4
4088 4087 4090 4089 4093 4085 4090 4084 
5
2945 2946 2950 2948 2942 2943 2948 2947 
6
670 667 669 671 670 670 668 671 
7
8869 8869 8873 8875 8870 8872 8871 8873 
8
1709 1707 1712 1712 1714 1710 1706 1712 
9
10239 10248 10242 10240 10242 10242 10245 10235 
10
6580 6579 6574 6580 6583 6580 6577 6581 

```

output-

```
#1 6 2 2 9 4 1 3 0 
#2 9 7 9 5 4 3 8 0 
#3 8 7 1 6 4 3 5 0 
#4 7 5 8 4 8 1 3 0 
#5 3 8 7 4 4 7 4 0 
#6 6 7 5 9 6 8 5 0 
#7 7 6 8 3 2 5 6 0 
#8 9 2 1 7 3 6 3 0 
#9 4 7 8 1 2 8 4 0 
#10 6 8 9 5 8 5 2 0 

```

해설코드 

```
for t in range(1,11):
    n=int(input())
    lst=list(map(int,input().split()))

    while lst[-1]!=0:
        a1=lst[0]-1
        if a1<=0:
            a1=0
            lst.append(a1)
            lst.remove(lst[0])
            break
        lst.append(a1)
        lst.remove(lst[0])
        a2=lst[0]-2
        if a2<=0:
            a2=0
            lst.append(a2)
            lst.remove(lst[0])
            break
        lst.append(a2)
        lst.remove(lst[0])
        a3 = lst[0] - 3
        if a3<=0:
            a3=0
            lst.append(a3)
            lst.remove(lst[0])
            break
        lst.append(a3)
        lst.remove(lst[0])
        a4 = lst[0] - 4
        if a4<=0:
            a4=0
            lst.append(a4)
            lst.remove(lst[0])
            break
        lst.append(a4)
        lst.remove(lst[0])
        a5 = lst[0] - 5
        if a5<=0:
            a5=0
            lst.append(a5)
            lst.remove(lst[0])
            break
        lst.append(a5)
        lst.remove(lst[0])
    print(f'#{t}',end=" ")
    for i in (lst):
        print(i, end=" ")
    print()



```



아니왜 이거면 되는거 같은데 

```
for t in range(1,11):
    n=int(input())
    lst=eval(input())
    print(f'#{t} {lst}')
```

