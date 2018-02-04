from node.node import Node
import queue

# Creates tree
a = Node('root')

b1 = Node('b1')
b2 = Node('b2')

a.add_child(b1)
a.add_child(b2)

c1 = Node('c1')
c2 = Node('c2')
c3 = Node('c3')
c4 = Node('c4')

b1.add_child(c1)
b1.add_child(c2)

b2.add_child(c3)
b2.add_child(c4)

try:
    a.add_child(1)
except ValueError:
    print("Trying to add non node raises Value Error")

bfs_q = queue.Queue()

bfs_q.put(a)

seen = []

while not bfs_q.empty():
    current_node = bfs_q.get()
    current_node_parent = current_node.get_parent()
    print(current_node.value)
    for c in current_node.children:
        bfs_q.put(c)