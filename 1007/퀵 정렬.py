def partition(arr,left,right):
    pivot=arr[left]
    i=left
    j=right
    while i <=j:
        while i<=j and pivot >= arr[i]:
            i+=1
        while i<=j and pivot <=arr[j]:
            j-=1
        if i <j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[left],arr[j]=arr[j],arr[left]
    return j
def quicksort(arr,left,right):
    if left>=right:
        return
    pivot_idx=partition(arr,left,right)
    quicksort(arr,left,pivot_idx -1)
    quicksort(arr,pivot_idx +1, right)
T= int(input())
for t in range(1,T+1):
    N=int(input())
    in_arr=list(map(int,input().split()))
    quicksort(in_arr,0,len(in_arr)-1)
    print(f'#{t} {in_arr[N//2]}')

# 틀린풀이 
# def quick_sorted(arr):
#     if len(arr) > 1:
#         pivot = arr[len(arr)-1]
#         left, mid, right = [], [], []
#         for i in range(len(arr)-1):
#             if arr[i] < pivot:
#                 left.append(arr[i])
#             elif arr[i] > pivot:
#                 right.append(arr[i])
#             else:
#                 mid.append(arr[i])
#         mid.append(pivot)
#         return quick_sorted(left) + mid + quick_sorted(right)
#     else:
#         return arr

# T=int(input())
# for t in range(1,T+1):
#     n=int(input())
#     arr=list(map,int(input().split()))
#     print(arr)
#     lista=quick_sorted(arr)
#     print(f'#{t} {lista[n//2]}')
