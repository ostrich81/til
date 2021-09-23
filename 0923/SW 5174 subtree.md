# SW 5174 subtree

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AXsHTyBaqJgDFARX&contestProbId=AXGBLnRKVf8DFARK&probBoxId=AXwQCMTKAOoDFATv&type=USER&problemBoxTitle=20210923&problemBoxCnt=4)

문제 요약 

​	1. 트리만들고 갯수세기

input - 

```
3
5 1
2 1 2 5 1 6 5 3 6 4 
5 1
2 6 6 4 6 5 4 1 5 3 
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
```

output-

```
#1 3
#2 1
#3 3
```

해설코드 

```
def f(n): # 순회하는 함수
    global cnt
    if n:
        cnt +=1
        f(ch1[n]) #왼쪽
        f(ch2[n]) #오른쪽

T=int(input())
for t in range(1,T+1):
    E,N=map(int,input().split())
    V=E+1 # 1부터 V까지 정점번호
    ch1=[0]*(V+1) # 자식1혹은 왼쪽자식 ,부모를 인덱스로 자식번호 저장
    ch2 = [0] * (V + 1) # 자식2 혹은 오른쪽 자식
    arr = list(map(int,input().split()))
    for i in range(E):
        n1,n2=arr[i*2],arr[i*2+1] #부모 n1 자식 n2
        if ch1[n1] ==0: #자식1이 없으면
            ch1[n1]=n2
        else:
            ch2[n1]=n2
    cnt=0 # 방문한 정점수
    f(N) # N부터 순회
    print(f'#{t} {cnt}')
```

