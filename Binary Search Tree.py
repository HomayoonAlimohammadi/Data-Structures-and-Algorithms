class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    
    def __str__(self):
        return f'''[Value: {self.value}
    \tLeft: {self.left}
    \tRight: {self.right}]
    '''


class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
        self.max_depth = 1

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
        self.max_depth += 1
        return self

    def contains(self, value):
        lookup_node = self.root
        while lookup_node is not None:
            if lookup_node.value > value:
                lookup_node = lookup_node.left
            
            elif lookup_node.value < value:
                lookup_node = lookup_node.right
            
            else:
                return True
        return False

    def __str__(self):
        return str(self.root)




bst = BinarySearchTree(10)
bst.insert(20)
bst.insert(9)
bst.insert(5)
bst.insert(9.5)
bst.insert(25)
print(bst)
print([
    bst.contains(1),
    bst.contains(20),
    bst.contains(10),
    bst.contains(25),
    bst.contains(5),
    bst.contains(9.5),
])