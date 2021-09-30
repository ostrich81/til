T=int(input())
for t in range(1,T+1):
    N , M= map(int,input().split())
    jin=list(map(str,str(bin(M))[2:]))[-N:]
    if len(jin)<N:
        answer='OFF'
    else:
        if '0' in jin:
            answer='OFF'
        else:
            answer='ON'
    print(f'#{t} {answer}')
