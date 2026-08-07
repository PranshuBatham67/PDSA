class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        parentU = self.find(u)
        parentV = self.find(v)

        if parentU == parentV:
            return

        if self.rank[parentU] < self.rank[parentV]:
            self.parent[parentU] = parentV
        elif self.rank[parentU] > self.rank[parentV]:
            self.parent[parentV] = parentU
        else:
            self.parent[parentV] = parentU
            self.rank[parentU] += 1


def kruskal(WL):
    vertices = len(WL)

    # Step 1: Convert adjacency list to edge list
    edges = []
    for u in WL:
        for v, weight in WL[u]:
            # Prevent duplicate edges in an undirected graph
            if u < v:
                edges.append((u, v, weight))

    # Step 2: Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Step 3: Create Union-Find
    uf = UnionFind(vertices)

    mst_cost = 0
    mst_edges = []

    # Step 4: Process each edge
    for u, v, weight in edges:

        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_cost += weight
            mst_edges.append((u, v, weight))

    return mst_cost, mst_edges
# Example Graph
edge = [
    (0,1,10),(0,2,18),(0,3,6),(0,4,20),(0,5,13),
    (1,2,10),(1,3,10),(1,4,5),(1,5,7),
    (2,3,2),(2,4,14),(2,5,15),
    (3,4,17),(3,5,12),
    (4,5,10)
]

size = 6

WL = {}
for i in range(size):
    WL[i] = []

for (i, j, d) in edge:
    WL[i].append((j, d))

cost, mst = kruskal(WL)

print("MST Cost:", cost)
print("Edges in MST:")
for e in mst:
    print(e)
