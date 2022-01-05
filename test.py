def insert_after(self, previous_node, data):
    new_node = Node(data)
    # 가장 마지막 순서 삽입
    if previous_node is self.tail:
        self.tail.next = new_node
        self.tail = new_node
    else: # 두 노드 사이에 삽입
        new_node.next = previous_node.next
        previous_node.next = new_node
        
self.tail.next = new_node
self.tail = new_node

data = previos_node.next.data

if previous_node.next is self.tail:
    previous_node.next = None
    self.tail = previous_node
else:
    previous_node.next = previous_node.next.next

retrun data