# 괄호검사

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

두 종류 가로가 있다.

1. 매칭이 잘 된 가로면 1 아니면 0출력 

   

input - 

```
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
```

output-

```
#1 1
#2 1
#3 0
```

제출코드 

```
T=int(input())
for t in range(1,T+1):
    testa=list(input())
    # print(testa)
    galho=[]
    answer=1
    an=[]
    for i in range(len(testa)):
        if testa[i]=='('  or  testa[i]==')' or testa[i]=='{' or  testa[i]=='}':
            galho +=testa[i]
            # print(galho)
    if galho.count('(') != galho.count(')'):
        answer=0
    elif galho.count('{') != galho.count('}'):
        answer=0
    else:
        for i in range(len(galho)):
            if galho[i]=='(' :
                answer -= 1
                an +=('k')
            elif galho[i]=='{':
                answer -= 2
                an += ('g')
            elif galho[i]==')' :
                answer +=1
                an.remove('k')
                # print(an)
                if len(an)==0:
                    answer=0
                    break
                elif answer >=2:
                    answer=0
                    break
            elif  galho[i]=='}':
                answer += 2
                an.remove('g')
                # print(an)
                if len(an) == 0:
                    answer = 0
                    break
                elif answer >= 2:
                    answer = 0
                    break
                # print(an)

    # print(an)


    print(f'#{t} {answer}')
```

테스트 케이스 10개중 9개는 맞는데 ({)} 이런경우를 못맞춘거같다.

```
T=int(input())
for t in range(1,T+1):
    s = input()
    stack=[]
    ans=1
    for x in s:
        if x =='(' or x== '{': #  여는 괄호 인경우
            stack.append(x)                            #push(x)
        elif x==')':
            #닫는 괄호인 경우
            if len(stack)==0:
                ans=0
                break
            if stack.pop()!='(':                        # 스택을 검사해야됨 먼저 =-> pop을 해야됨 - 전제조건 스택이 비어있지 않아야함
                ans=0
                break

        elif  x == '}':
            if len(stack)==0:
                ans=0
                break
            if stack.pop()!='{':
                ans=0
                break
                #짝이 맞는지 비교
        else:                       #괄호가 아닌경우 ..
          pass
    # print(stack)
    if stack: #닫는 괄호가 부족한 경우
        ans=0
    print(f'#{t} {ans}')
```

