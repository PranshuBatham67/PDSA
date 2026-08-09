class minHeap:
    def __init__(self):
        self.A = []
    
    
    def min_heapify(self, ele_idx):
        left_chld = 2*ele_idx + 1
        right_chld = 2*ele_idx + 2
        smallest = ele_idx
        
        #case1: if left_chld < smallest 
        if left_chld < len(self.A) and self.A[left_chld] < self.A[smallest]:
            smallest = left_chld
        #case2: if right_chld < smallest
        if right_chld < len(self.A) and self.A[right_chld] < self.A[smallest]:
            smallest = right_chld 
        # swap if smallest is not ele_idx
        if smallest != ele_idx:
            (A[ele_idx], A[smallest]) = (A[smallest], A[ele_idx])
            
    
    def build_min_heap(self, L):
        for i in L:
            self.A.append(i)
            
        parent_idx = int((len(self.A)//2) - 1)
        for i in range(parent_idx, -1, -1):
            self.min_heapify(i)
        
    def min_insert(self, ele):
        self.A.append(ele)
        last_idx = len(self.A) - 1
        
        while last_idx > 0:
            parent_idx = int(len(self.A)//2 - 1)
            if self.A[last_idx] < self.A[parent_idx]:
                (slef.A[last_idx], self.A[parent_idx]) = (self.A[parent_idx], self.A[last_idx])
                last_idx = parent_idx
            else:
                break
            
    def delete_min(self):
        item = None
        if self.A != []:
            self.A[0],self.A[-1] = self.A[-1],self.A[0]
            item = self.A.pop()
            self.min_heapify(0)
        return item

        
        
        
        
        
        
        
        
        
        
        
        
        
        
