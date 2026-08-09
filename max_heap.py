class maxHeap:
    def __init__(self):
        self.A = []
        
    def max_heapify(self, ele_idx):
        left_cld = 2*ele_idx + 1
        right_cld = 2*ele_idx + 2
        largest = ele_idx #initially ele_idx is my largest value
        
        #case1: if left_child is greater then A[K]
        if left_child < len(self.A) and A[left_child] > A[largest]:
            largest = left_child
        #case2: if right_child is greater than A[K]
        if right_child < len(self.A) and A[right_child] > A[largest]:
            largest = right_child
            
        #swapping after deciding largest element
        if largest != ele_idx:
            (A[ele_idx], A[largest]) = (A[largest], A[ele_idx])
            self.heapify(largest)
            
    def build_max_heap(self, L):
        for i in L:
            self.A.append(i)
        
        # parent element idx : n//2 - 1 
        parent_idx = int(len(self.A)//2 - 1)
        
        for k in range(parent_idx, -1, -1):
            self.heapify(k)
            
    
    def max_heap_insert(self, ele):
        #step1: append ele in last
        self.A.append(ele)
        #step2: last idx of array
        last_idx = len(self.A) - 1
        while last_idx > 0:
            #step3: get the parent idx
            parent_idx = last_idx//2 - 1
            #case: if element at last_idx is greater than element at parent_idx then swap it.
            if self.A[last_idx] > self.A[parent_idx]:
                (self.A[parent_idx], self.A[last_idx]) = (self.A[last_idx], self.A[parent_idx])
                
            else:
                break
        
    def max_heap_delete(self, ele): # Need to return element which we delete
        # In deletion we delete the first element means element at the first idx
        item = None
        if self.A != []:
            # swap the element at first and last idx
            (self.A[0], self.A[-1]) = (self.A[-1], self.A[0])
            # pop the last element now
            item = self.A.pop()
            # now max heap may not be max heap so we need to fix it.
            self.heapify(0)
        
        return item
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
