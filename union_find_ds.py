class find_union_ds:
    def __init__(self, size):
        self.size = size
        self.parent = []
        self.rank = []
        
        
    def make_union_find(self):
        for i in range(self.size):
            self.parent.append(i)
            self.rank.append(0)
        
        return 
    
    def find(self, node):
        # Path Compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self, u,v):
        # find parent of both elements u and v.
        parentU = self.find(u)
        parentV = self.find(v)
        
        # case1 : if parents are same
        if(parentV == parentU):
            return
        # case2: if rank of both elements v and u are same then we can add any of them with any one.
        elif (self.rank[parentU] == self.rank[parentV]):
            self.parent[parentV] = parentU
            self.rank[parentU] +=1
            return
            
        elif(self.rank[parentU] > self.rank[parentV]):
            self.parent[parentV] = parentU
            return
        else:
            self.parent[parentU] = parentV
            

uf = find_union_ds(7)
uf.make_union_find()

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
uf.union(5, 6)
uf.union(2, 4)

print(uf.parent)
print(uf.rank)

print(uf.find(0))
print(uf.find(4))
print(uf.find(6))
            
            
            
            
            
            
            
            
