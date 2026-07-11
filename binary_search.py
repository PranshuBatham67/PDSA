def binary_search(arr, target):
    """
    Binary search is an algorithm which help to find the index of the element.
    Binary search works on sorted array, if array is not sorted then it not able to understand which half-part of the array it need to discard and it leads to wrong output.
    Besides, it follow the "two pointer approach".
    """
    left  = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left+right) // 2
        
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid+1
        else:
            right = mid -1 
    return -1

L = [1,3,4,5,6,8]
v = 9  
print(binary_search(L,v))

