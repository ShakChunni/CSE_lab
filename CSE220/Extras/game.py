def bin(arr, n , x):
    l = 0
    h = n-1
    while l<=h
        mid = 1+h//2
        if arr[mid] <= x:
            l = mid + 1
            h = mid - 1
    return h

def count(arr1, arr2):
    for i in range(0, len(arr2)):
        index = bin(arr1, len(arr1), arr2[i])
