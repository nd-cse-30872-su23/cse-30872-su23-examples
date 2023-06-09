#!/usr/bin/env python3

# Exercise 09-B: Binary Tree Min

import collections
import sys

# Structures

Node = collections.namedtuple('Node', 'value left right')

# Functions

def minimum_tree(root: Node) -> int:
    ''' Use divide and conquer to compute the minimum of binary tree '''
    # Divide and conquer: recursively solve left and right sub-trees
    left_min  = minimum_tree(root.left)  if root.left  else root.value
    right_min = minimum_tree(root.right) if root.right else root.value

    # Combine: take minimum of current node and left and right minimums
    return min(root.value, left_min, right_min)

# Main Execution

def main() -> None:
    # Create tree
    root = Node(7,
        Node(5,
                Node(3, None, None),
                None),
        Node(4,
                None,
                Node(2, None, None),
    ))

    # Compute minimum of tree
    print(minimum_tree(root))

if __name__ == '__main__':
    main()
