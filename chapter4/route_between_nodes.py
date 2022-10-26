from collections import deque
from tkinter import E

# VISUAL OF TEST GRAPH:

# A -- B
# |    |
# C -- D
# |
# E -- F -- G -- H
#      | \
#      O   I -- J -- K
#               |
#               L

# P -- Q
# |  /
# R
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"],
    "P": ["Q", "R"],
    "Q": ["P", "R"],
    "R": ["P", "Q"],
}

def is_route_bfs(graph,start,end):
    if start == end:
        return True
    Q = deque()
    visited = set()
    Q.append(start)
    while len(Q) != 0:
        tmp = Q.popleft()
        if tmp == end:
            return True
        for c in graph[tmp]:
            if c not in visited:
                visited.add(c)
                Q.append(c)
    return False

        
def is_route_dfs(graph,start,end,visited=None):
    if visited is None:
        visited = set()
    for c in graph[start]:
        if c not in visited:
            visited.add(c)
            if c == end or is_route_dfs(graph,c,end,visited):
                return True
    return False


if __name__=="__main__":
    print(is_route_dfs(graph,"A","L"))

