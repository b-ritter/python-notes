class Node():
    def __init__(self, value=None):
        self.children = []
        self.parent = None
        self.value = value
    
    def add_child(self, node):
        if type(node).__name__ == 'Node':
            node.parent = self
            self.children.append(node)
        else:
            raise ValueError
    
    def get_parent(self):
        return self.parent.value if self.parent else 'root'