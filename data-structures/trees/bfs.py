from node.node import Node

a = Node('foo')

print(a.value)

b = Node('bar')

a.add_child(b)

try:
    a.add_child(1)
except ValueError:
    print("Trying to add non node raises Value Error")

print(type(a.children.pop()).__name__)