def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p]<tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c1 = 2*p
    c2 = 2*p + 1
    while c1<=last:     # 자식이 하나라도 있으면
        if c2<=last:     # 자식이 둘이면
            if tree[c1]>=tree[c2] and tree[c1]>tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
                p = c1
            elif tree[c1]<tree[c2] and tree[c2]>tree[p]:
                tree[c2], tree[p] = tree[p], tree[c2]
                p = c2
            c1 = p*2
            c2 = p*2+1
        else:           # 왼쪽자식만 있는 경우
            if tree[c1]>tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
            break
    return tmp

tree = [0]*101      # 최대 100번노드까지..  최대힙
last = 0            # 마지막 노드 번호
#2
# def enq(data):
#     global hsize
#     hsize += 1
#     H[hsize] = item

#     c = hsize
#     p = hsize // 2

#     while p and H[p] > H[c]:
#         H[p], H[c] = H[c], H[p]
#         c = p
#         p = c // 2

# def deq():
#     global hsize
#     tmp = H[1]
#     H[1] = H[hsize]
#     hsize -= 1
#     p = 1
#     c = p * 2  # 왼쪽자식번호를 먼저 계산해서 

#     while c <= hsize: # 왼쪽 자식이 있는지 확인
#         if c + 1 <= hsize and H[c] > H[c + 1]: # 오른쪽 자식도 있고 오른쪽이 더 작으면 선택
#             c += 1
#         if H[p] > H[c]:  # 부모와 자식 비교
#             H[p], H[c] = H[c], H[p] # 자식이 더 작으면 교환
#             p = c           # 자리 바꿔서 자식 자리로 간 값과 그 자리의 자식번호 계산
#             c = p * 2
#         else:
#             break

#     return tmp