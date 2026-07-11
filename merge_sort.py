def merge(A,B):
    n = len(A)
    m = len(B)
    
    # new variable and data structure
    (C,i,j) = ([],0,0)
    
    # case1 : check all element from both element one by one
    while i<n and j<m:
        if A[i] <= B[j]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[i])
            j+=1
            
    # case2: if A's elements are finished, append all element of B to C
    while j < m:
        C.append(B[j])
        j+=1
        
    # case3: if B's element are finished, append all element of A to C
    while i<n:
        C.append(A[i])
        i+=1
    return C
def merge_sort(arr):
    """
    In the merge_sort, we divide the list from its middle and pass both part into the function.
    
    Then we we pass both lists one by one in own function through resucrsion.
    
    After passing both list, we take each element from both element one by one and check which one is less or bigger, after checking we put both element into another list in ascending order.
    
    While taking element if one list's element is finished and another one's remaining then we append all remaining element into the new list which we created earlier.
    """
    n = len(arr)
    
    if n<=1:
        return arr
        
    mid = n//2
    
    # passing element in own function - resucrsion
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    result = merge(left_arr, right_arr)
    return result
    
L = [4,2,7,6,8,3,5,1]
print(merge_sort(L))
    
