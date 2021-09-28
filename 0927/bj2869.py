A,B,V=list(map(int,input().split()))
answer= (V-B)/(A-B)
print(int(answer) if answer== int(answer) else int(answer)+1)