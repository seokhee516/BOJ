class Node:
    def __init__(self, data, left_child,right_child):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

def preorder(node):
    if node.data != '.':
        print(node.data, end='')
        if node.left_child != '.':
            preorder(tree[node.left_child])
        if node.right_child != '.':
            preorder(tree[node.right_child])

def inorder(node):
    if node.data != '.':
        if node.left_child != '.':
            inorder(tree[node.left_child])
        print(node.data, end='')
        if node.right_child != '.':
            inorder(tree[node.right_child])

def postorder(node):
    if node.left_child != '.':
        postorder(tree[node.left_child])
    if node.right_child != '.':
        postorder(tree[node.right_child])
    if node.data != '.':
        print(node.data, end='')

import sys
N = int(sys.stdin.readline().strip())
tree = {}
for _ in range(N):
    node, left, right = map(str, sys.stdin.readline().strip().split())
    tree[node] = Node(node,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])