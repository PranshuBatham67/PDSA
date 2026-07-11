def insertionsort(L):
    """
    Inside the insertion sort, it takes the element and sort by its all previous elements.
    """
    
    n = len(L)
    
    if n<1:
        return L
        
        
    for current_ele_pos in range(n):
        next_ele_pos = current_ele_pos
        
        while(next_ele_pos > 0 and L[next_ele_pos] < L[next_ele_pos-1]):
            # swap
            (L[next_ele_pos], L[next_ele_pos-1])  = (L[next_ele_pos-1], L[next_ele_pos])
            next_ele_pos -= 1
            
    return L
    
    
L = [5,6,3,2,4,1]
print(insertionsort(L))
