def single_source(WList, s):
    infinity = 1 + len(WList.keys())*max([d for u in WList.keys() for (v,d) in WList[u]])
    
    # we need to store the key-value pair of who visited and each vertex's distance.
    (visited, distance) = ({}, {})
    
    # make every vertex visited false and distance infinity
    for i in WList.keys():
        (visited[i], distance[i]) = (False, infinity)
    distance[s] = 0
    
    for u in WList.keys():
        # Find minimum distance value on vertices which are not visited
        min_dist = min([distance[v] for v in WList.keys() if not visited[v]])
        # Find vertices which have minimum distance value min_dist
        min_vertex = min([v for v in WList.keys() if not visited[v] and distance[v] == min_dist])
        # Select minimum level vertex which have minimum distance value min_dist and mark visited
        visited[min_vertex] = True
        # Check for each adjacent of nextv vertex which is not visited
        for (u,d) in WList[min_vertex]:
            if not visited[u]:
                if distance[min_vertex] + d < distance[u]:
                    distance[u] = distance[min_vertex] + d
    return distance


dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7

WList = {}
"""
WList = {
    0: [(1,10), (2,80)],
    1: [(2,6), (4,20)],
    2: [(3,70)],
    3: [],
    4: [(5,50), (6,5)],
    5: [(6,10)],
    6: []
}
"""
for i in range(size):
    WList[i] = []
    
for (v,u,d) in dedges:
    WList[v].append((u,d))
    
print(single_source(WList, 0))
