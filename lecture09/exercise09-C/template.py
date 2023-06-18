#!/usr/bin/env python3

# Exericse 09-C: Binary Tree Height

import collections

# Structures

Node = collections.namedtuple('Node', 'value left right')

# Functions

def height_tree(root: Node) -> int:
    ''' Use divide and conquer to compute the height of binary tree '''
    # Base case: Non-existent node
    pass

    # Divide and conquer: recursively solve left and right sub-trees
    pass

    # Combine: take max sub-tree height and add 1
    pass

# Main Execution

def main() -> None:
    # Create tree
    root = Node(7,
        Node(5,
                Node(3, Node(6, None, None), None),
                None),
        Node(4,
                None,
                Node(2, None, None),
    ))

    # Compute height of tree
    print(height_tree (root))

if __name__ == '__main__':
    main()
