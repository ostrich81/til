def dfs(idx,_sum):
    global answer
    if answer < _sum:
        return
    if idx >= N:
        answer= _sum
        return
    count= station[idx]
    for i in range(count,0,-1):
        dfs(idx+1,_sum+1)

T=int(input())
for t in range(1,T+1):
    answer=float('inf')
    station = list(map(int,input().split()))
    N=station.pop(0) -1
    dfs(0,-1)
    print(f'#{t} {answer}')