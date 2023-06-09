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
    # TODO: Use divide and conquer to parse tree
    pass

def walk_tree(root: Node) -> list[int]:
    # TODO: Use BFS Traversal with Queue to create list of values
    pass

def dump_tree(root: Node) -> None:
    print(','.join(map(str, walk_tree(root))))

def invert_tree(root: Node) -> None:
    # TODO: Use divide and conquer to invert binary tree
    pass

# Main Execution

def main() -> None:
    for line in sys.stdin:
        values = list(map(int, line.split()))
        root   = read_tree(values)

        invert_tree(root)
        dump_tree(root)

if __name__ == '__main__':
    main()
