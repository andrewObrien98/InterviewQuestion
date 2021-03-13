"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(node, k, floor=None, ceil=None):
    if node == None and (floor == None or ceil == None):
        print("(neither, neither)")
        return
    elif node == None:
        print("(" + str(floor) + ", " + str(ceil) + ")")
        return
    if node.value >= k:
        return findCeilingFloor(node.left, k, node.value, ceil)
    else:
        return findCeilingFloor(node.right, k, floor, node.value)

# Fill this in.

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

findCeilingFloor(root, 7)
# (4, 6)