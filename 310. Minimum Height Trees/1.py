from collections import defaultdict
from typing import List
n = 4
edges = [[1,0],[1,2],[1,3]]

def findMinHeightTrees( n: int, edges: List[List[int]]) -> List[int]:
    # 0: 1
    # 1: 0, 2, 3
    # 2: 1
    # 3: 1
    # q = [0, 2, 3]
    # temp = []
    
    if not edges:
        return [0]
    graph = defaultdict(set)
    for x,y in edges:
        graph[x].add(y)
        graph[y].add(x)
    
    q = []
    for k,v in graph.items():
        if len(v) < 2:
            q += [k]
    temp = []
    while True:
        for node in q:
            for n in graph[node]:
                graph[n].remove(node)
                if len(graph[n]) == 1:
                    temp += [n]
        if not temp:
            break
        temp, q = [], temp
        
    return q

findMinHeightTrees(n, edges)