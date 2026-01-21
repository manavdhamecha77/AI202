"""
0  = Chicago
1  = Detroit
2  = Cleveland
3  = Indianapolis
4  = Columbus
5  = Pittsburgh
6  = Buffalo
7  = Syracuse
8  = New York
9  = Philadelphia
10 = Baltimore
11 = Boston
12 = Providence
13 = Portland

Chicago - Detroit       283
Chicago - Cleveland     345
Chicago - Indianapolis  182
Detroit - Cleveland     169
Detroit - Buffalo       256
Cleveland - Buffalo     189
Cleveland - Pittsburgh  134
Cleveland - Columbus    144
Indianapolis - Columbus 176
Columbus - Pittsburgh   185
Pittsburgh - Buffalo    215
Pittsburgh - Philadelphia 305
Pittsburgh - Baltimore  247
Buffalo - Syracuse      150
Syracuse - New York     254
Syracuse - Boston       312
New York - Philadelphia 97
New York - Providence   181
Philadelphia - Baltimore 101
Philadelphia - Boston   215
Boston - Providence     50
Boston - Portland       107


Implement Breadth First Search(BFS) and Depth First Search (DFS) algorithm to find all
possible step cost between Syracuce to Chicago.

"""

from collection import queue, stack

graph = {
    0 : [(1,283), (2,345), (3,182)],               
    1 : [(0,283), (2,169), (6,256)],               
    2 : [(0,345), (1,169), (6,189), (5,134), (4,144)], 
    3 : [(0,182), (4,176)],                        
    4 : [(3,176), (2,144), (5,185)],               
    5 : [(2,134), (4,185), (6,215), (9,305), (10,247)], 
    6 : [(1,256), (2,189), (5,215), (7,150)],      
    7 : [(6,150), (8,254), (11,312)],              
    8 : [(7,254), (9,97), (12,181)],               
    9 : [(8,97), (5,305), (10,101), (11,215)],     
    10: [(5,247), (9,101)],                       
    11: [(7,312), (9,215), (12,50), (13,107)],    
    12: [(11,50), (8,181)],                       
    13: [(11,107)]                                
}

def dfs(graph, start, target):
    all_paths = []
    s = stack(126)
    s.push([start, [start], 0])

    while len(s.container) > 0: # not empty
        node, path, cost = s.pop()
        if node == target: # if visited stop
            all_paths.append({"path": path, "cost": cost})
            continue
        for neighbor, step_cost in graph[node]:
            if neighbor not in path:
                s.push([neighbor, path + [neighbor], cost + step_cost]) # add
    return all_paths

def bfs(graph, start, target):
    all_paths = []
    q = queue(126)  
    q.push([start, [start], 0]) # node, path array, cost

    while len(q.container) > 0: # not empty
        node, path, cost = q.pop()
        if node == target:
            all_paths.append({"path": path, "cost": cost})
            continue
        for neighbor, step_cost in graph[node]:
            if neighbor not in path:
                q.push([neighbor, path + [neighbor], cost + step_cost])
    return all_paths


dfs_paths = dfs(graph, 7, 0)
bfs_paths = bfs(graph, 7, 0)

# countb = 0
# countd = 0

print("DFS Paths:")
for p in dfs_paths:
    # countd += 1
    print(p)

print("\nBFS Paths:")
for p in bfs_paths:
    # countb += 1
    print(p)
