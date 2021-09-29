T = int(input())
for t in range(1,T+1):
    lista=list(map(int,input()))
    ans=[]
    dec=0
    for i in range(70):
        j=6-i%7
        dec += lista[i]*(1<<j)
        if j==0:
            ans.append(dec)
            dec=0
    print(f'#{t}',*ans)


