import BST 


def DFS_PO(tree, seen=[]):

    if len(seen) == 0:
        seen.append(tree.root)

    location = seen[-1]
    if location.left:
        seen.append(location.left)
        DFS_PO(tree, seen)
    if location.right:
        seen.append(location.right)
        DFS_PO(tree, seen)

    return seen



def main():
    tree = BST.BinarySearchTree(47)
    tree.insert(21)
    tree.insert(76)
    tree.insert(18)
    tree.insert(27)
    tree.insert(52)
    tree.insert(82)

    seen = DFS_PO(tree)
    print([node.value for node in seen])


if __name__ == '__main__':
    main()