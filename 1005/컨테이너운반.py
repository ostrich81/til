T=int(input())
for t in range(1,T+1):
    answer=0
    N,M=map(int,input().split())
    lista=sorted(list(map(int,input().split())))
    listb=sorted(list(map(int,input().split())))
    while lista and listb:
        truck= listb.pop()
        while lista:
            container = lista.pop()
            if truck >=container:
                answer+= container
                break
    print(f'#{t} {answer}')