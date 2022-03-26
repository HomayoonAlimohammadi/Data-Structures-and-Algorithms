class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'Value: {self.value}, Left: {self.left}, Right: {self.right}'


class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.depth = 1

    def insert(self, value):
        new_node = Node(value)
        lookup_node = self.root
        while True:
            if lookup_node.value > new_node.value:
                if lookup_node.left is None:
                    lookup_node.left = new_node
                    break
                else:
                    lookup_node = lookup_node.left
            
            elif lookup_node.value < new_node.value:
                if lookup_node.right is None:
                    lookup_node.right = new_node
                    break
                else:
                    lookup_node = lookup_node.right
                    
    

