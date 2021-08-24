# sw 5일차 Forth

문제출처 - [SW Expert Academy](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

문제 요약 

 	1. 후위 계산식 스택구현

input - 

```
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
 
```

output-

```
#1 84
#2 error
#3 168
```

해설코드 

```
T=int(input())
for t in range(1,T+1):
    lst=list(input().split())
    stack=[]
    answer=[]
    for x in lst:
        if x==".":
            if len(stack)==1:       # 0이나 2일 경우 모두 고려해 줘야됨 이거때문에 계속 10테케중 9 패스. ..... 
                answer.append(stack[0])
            else:
                answer.append('error')
        elif x=="+":
            if len(stack)<=1:
                answer.append('error')
                break
            else:
                op1 = stack.pop()
                op2=stack.pop()
                stack.append(op2+op1)
        elif x=="*":
            if len(stack)<=1:
                answer.append('error')
                break
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2*op1)
        elif x=="-":
            if len(stack)<=1:
                answer.append('error')
                break
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2-op1)
        elif x=="/":
            if len(stack)<=1:
                answer.append('error')
                break
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2//op1)
        else :
            stack.append(int(x))
    print(f'#{t} {answer[0]}')
```



