T= int(input())
for t in range(1,T+1):
    N, array=input().split()
    print(f'#{t}', end=' ')
    for i in array:
        binary=bin(int(i,16))[2:]
        print('0'*(4-len(binary)) +binary, end='')
    print()
