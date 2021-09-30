T=int(input())
for t in range(1,T+1):
    answer=''
    number=float(input())
    one=1
    for _ in range(12):
        one *=0.5
        if number-one >=0:
            answer+='1'
            number -=one
            if not number:
                break
        else:
            answer +='0'
    if number:
        answer='overflow'
    print(f'#{t} {answer}')