import BST 

def BFS(tree):
    queue = []
    results = []
    queue.append(tree.root)
    while len(queue) != 0:
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)

        # Storing only the value of nodes
        results.append(queue[0].value) 
        queue = queue[1:]
    
    return results

tree = BST.BinarySearchTree(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)

print(BFS(tree))

