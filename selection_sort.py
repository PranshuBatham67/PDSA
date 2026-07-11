def selection_sort(arr):
    """
    Selection sort is an sorting technique who is reponsible for sorting the unsorted array.
    
    In this, we try to find the minimum element position and swap.
    So, basically we select the minimum element from the L[i+1: ] and swap it with L[i].
    """
    for i in range(len(arr)):
        min_ele_pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ele_pos]:
                min_ele_pos = j
                
        # swapping
        (arr[i], arr[min_ele_pos]) = (arr[min_ele_pos], arr[i])
        
    return arr
    
    
L = [4,5,2,1,3]
print(selection_sort(L))
