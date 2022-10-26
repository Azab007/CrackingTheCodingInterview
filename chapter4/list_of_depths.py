from collections import deque
from linked_list import LinkedList
class Node:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def list_of_depths(root):

    Q = deque()
    levels = {}
    Q.append((root,0))
    while len(Q) != 0:
        node,level = Q.popleft()
        if level not in levels:
            levels[level] = LinkedList([])
        levels[level].add(node)
        if node.left:
            Q.append((node.left,level+1))
        if node.right:
            Q.append((node.right,level+1))

    return levels

if __name__=="__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    levels = list_of_depths(root)
    print(levels)


