def solution(nums):
    answer = 0
    limit=len(nums)//2
    print(limit)
    pick=list(set(nums))
    print(pick)
    if len(pick)>limit:
        answer=limit
    else:
        answer=len(pick)
    
    return answer