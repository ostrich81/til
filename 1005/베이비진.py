def M(number,index):
    global answer

    if number &1:
        player=player1
    else:
        player=player2
    if player[index] ==3:
        answer=number
    if index<8 and player[index] and player[index+1] and player[index+2]:
        answer=number
    if index>1 and player[index] and player[index-1] and player[index-2]:
        answer=number
    if 0< index <9 and player[index-1] and player[index] and player[index+1]:
        answer= number
T=int(input())
for t in range(1,T+1):
    answer=0
    player1=[0 for _ in range(10)]
    player2=[0 for _ in range(10)]
    card_list= list(map(int,input().split()))
    for i in range(12):
        if i &1:
            player2[card_list[i]]+= 1
            M(2,card_list[i])
        else:
            player1[card_list[i]] +=1
            M(1,card_list[i])
        if answer:
            break
    print(f'#{t} {answer}')