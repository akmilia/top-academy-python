# def two_sum(arr, sum):
#     i=0
#     j=1

#     i = arr[0] 

#     for k in range(0, len(arr)):
#         if arr[k]==sum-i:
#             j=arr[k]  

#     return [i, j]  

def two_sum(arr, sum): 
    i=0
    j=0
    dir={}

    for val in arr:
        if arr[i] in dir:
            return [dir[arr[i]] , i]
        dir[sum - arr[i]]=i 
    return [-1, 1]

arr = [1, 4, -2, 6, 7]

print(two_sum(arr, 5))
print(two_sum(arr, 2))
print(two_sum(arr, 11))
print(two_sum(arr, 4))
print(two_sum(arr, -1))
print(two_sum(arr, 13))