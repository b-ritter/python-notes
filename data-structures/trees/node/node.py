class Node():
    def __init__(self, value=None):
        self.children = []
        self.parent = None
        self.value = value
    
    def add_child(self, node):
        if type(node).__name__ == 'Node':
            self.children.append(node)
        else:
            raise ValueError