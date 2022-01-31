
import sys

def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    
    largest = index

    if 0 <left_child_index< tree_size and tree[left_child_index] > tree[index]:
        largest = left_child_index
    if 0 < right_child_index< tree_size and tree[right_child_index]>tree[index]:
        largest = right_child_index
    
    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)

def swap(tree, index1, index2):
    tree[index1], tree[index2] = tree[index2], tree[index1]

def reverse_heapify(tree, index):
    parent_index = index // 2
    if 0 < parent_index < len(tree) and tree[parent_index]<tree[index]:
        swap(tree, parent_index, index)
        reverse_heapify(tree, parent_index)

'''
heap = [None]
for _ in range(int(sys.stdin.readline().strip())):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        try:
            swap(heap, 1, len(heap)-1)
            return_value = heap.pop()
            heapify(heap, 1, len(heap))
            print(return_value)
        except IndexError:
            print(0)
    else:
        heap.append(x)
        reverse_heapify(heap, len(heap)-1)
'''

heap = [None]
for _ in range(int(sys.stdin.readline().strip())):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(heap.pop(1))
    else:
        heap.append(x)
        reverse_heapify(heap, len(heap)-1)