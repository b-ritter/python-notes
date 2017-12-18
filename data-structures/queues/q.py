import queue

q = queue.Queue(maxsize=3)

q.put(1)
q.put(2)
q.put(3)

# Should be True
print(q.full())

# Should be 1
print(q.get())

# Should be 2
print(q.get())

# Should be 3
print(q.get())

# Should be True
print(q.empty())