import re
from typing import List
from sys import maxsize
from collections import deque

all_nodes = []

def add_edge(adj: List[List[int]], src: int, dest: int) -> None:
    adj[src].append(dest)
    adj[dest].append(src)

# Function which finds all the paths
# and stores it in paths array
def find_paths(paths: List[List[int]], path: List[int],
               parent: List[List[int]], n: int, u: int) -> None:
    # Base Case
    if (u == -1):
        paths.append(path.copy())
        return
 
    # Loop for all the parents
    # of the given vertex
    for par in parent[u]:
 
        # Insert the current
        # vertex in path
        path.append(u)
 
        # Recursive call for its parent
        find_paths(paths, path, parent, n, par)
 
        # Remove the current vertex
        path.pop()
 
# Function which performs bfs
# from the given source vertex
def bfs(adj: List[List[int]],
        parent: List[List[int]], n: int,
        start: int) -> None:
 
    # dist will contain shortest distance
    # from start to every other vertex
    dist = [maxsize for _ in range(n)]
    q = deque()
 
    # Insert source vertex in queue and make
    # its parent -1 and distance 0
    q.append(start)
    parent[start] = [-1]
    dist[start] = 0
 
    # Until Queue is empty
    while q:
        u = q[0]
        q.popleft()
        for v in adj[u]:
            if (dist[v] > dist[u] + 1):
 
                # A shorter distance is found
                # So erase all the previous parents
                # and insert new parent u in parent[v]
                dist[v] = dist[u] + 1
                q.append(v)
                parent[v].clear()
                parent[v].append(u)
 
            elif (dist[v] == dist[u] + 1):
 
                # Another candidate parent for
                # shortes path found
                parent[v].append(u)
 
# Function which prints all the paths
# from start to end
def print_paths(adj: List[List[int]], n: int,
                start: int, end: int) -> None:
    paths = []
    path = []
    parent = [[] for _ in range(n)]
 
    # Function call to bfs
    bfs(adj, parent, n, start)
 
    # Function call to find_paths
    find_paths(paths, path, parent, n, end)
    for v in paths:
 
        # Since paths contain each
        # path in reverse order,
        # so reverse it
        v = reversed(v)
 
        # Print node for the current path
        for u in v:
            print('N'+ str(u), end = " ")
        print()

if __name__ == "__main__":
    my_string = "(N100,N33),(N44,N27),(N16,N44),(N1,N9),(N16,N22),(N49,N34),(N33,N16),(N22,N0),(N3,N16),(N41,N44),(N3,N35),(N27,N8),(N0,N8),(N9,N0),(N17,N35),(N26,N46)"

    # break text on commas outside parens
    # then inside
    # from node N0 to N100.

    my_pairs = [", ".join(x.split()) for x in re.split(r'[()]',my_string) if x.strip()]

    # Number of vertices
    n = 101
    adj = [[] for _ in range(n)]
    for node in my_pairs: 
        if node != ',':
            

            nodess = node.split(',')
            
            
                
            print("Found node {}".format(nodess[0]))
            print("Found node {}".format(nodess[1]))   
            add_edge(adj, int(nodess[0][1:]), int(nodess[1][1:]))
    # Given source and destination
    src = 0
    dest = 100
 
    # have to put the "N" back on 
    print_paths(adj, n, src, dest)

