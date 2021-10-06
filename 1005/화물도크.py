T=int(input())
for t in range(1,T+1):
    answer=1
    N=int(input())
    timelst=[list(map(int,input().split())) for _ in range(N)]
    timelst.sort(key=lambda x : x[1],reverse=True)
    endtime=timelst.pop()[1]
    while timelst:
        s,e = timelst.pop()
        if endtime <=s:
            endtime=e
            answer+=1

    print(f'#{t} {answer}')