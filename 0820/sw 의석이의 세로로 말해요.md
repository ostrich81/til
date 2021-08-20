# 의석이의 세로로 말해요

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AWVWgkP6sQ0DFAUO&solveclubId=AXsHTyBaqJgDFARX&problemBoxTitle=20210820_문제풀이1&problemBoxCnt=8&probBoxId=AXtSam9qcc0DFARW)

문제 요약 

 	1. 주어진 문자 세로로 읽기 

input - 

```

2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx	//Test Case 갯수
//Test Case #1의 시작




//Test Case #2의 시작


```

output-

```
#1 Aa0FfBb1GgCc2HhDd3IiEe4Jj
#2 Aa0aPAf985Bz1EhCz2W3D1gkD6x	//TC #1의 정답               
 
```

해설코드 

```
T= int(input())
for t in range(1,T+1):
    word=[0]*5
    maxlen=0
    for i in range(5):
        word[i]= list(input())
        if len(word[i])>maxlen:
            maxlen=len(word[i])
    print(f'#{t}',end=" ")
    for i in range(maxlen):
        for j in range(5):
            # case1
            # if len(word[j])>i:
            #     print(word[j][i], end='')
            # case2
            try:
                print(word[j][i], end ="")
            except:
                pass
    print()
```

