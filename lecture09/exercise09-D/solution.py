#!/usr/bin/env python3

# Exercise 09-D: Invert Binary Tree

import collections
import dataclasses
import sys

# Classes

@dataclasses.dataclass
class Node:
    value:  int
    left:   'Node'
    right:  'Node'

# Functions

def read_tree(values: list[int], index: int=0) -> Node|None:
    if index >= len(values):
        return None

    return Node(
        values[index], 
        read_tree(values, 2*index + 1), 
        read_tree(values, 2*index + 2)
    )

def walk_tree(root: Node) -> list[int]:
    # BFS Traversal with Queue
    nodes  = collections.deque([root])
    values = []

    while nodes:
        node = nodes.popleft()

        values.append(node.value)

        if node.left:  nodes.append(node.left)
        if node.right: nodes.append(node.right)

    return values

def dump_tree(root: Node) -> None:
    print(','.join(map(str, walk_tree(root))))

def invert_tree(root: Node) -> None:
    # Base case: No longer a Node
    if root is None:
        return

    # Divide and Conquer: Swap left and right and recurse
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

# Main Execution

def main() -> None:
    for line in sys.stdin:
        values = list(map(int, line.split()))
        root   = read_tree(values)
        #dump_tree(root)

        invert_tree(root)
        dump_tree(root)

if __name__ == '__main__':
    main()
