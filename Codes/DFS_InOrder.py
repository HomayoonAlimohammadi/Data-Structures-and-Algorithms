import BST


def DFS_InOrder(tree, seen=[], results=[]):

    if len(seen) == 0:
        seen.append(tree.root)

    location = seen[-1]
    if location.left:
        seen.append(location.left)
        DFS_InOrder(tree, seen)

    results.append(location)

    if location.right:
        seen.append(location.right)
        DFS_InOrder(tree, seen)

    return results


def main():
    tree = BST.BinarySearchTree(47)
    tree.insert(21)
    tree.insert(76)
    tree.insert(18)
    tree.insert(27)
    tree.insert(52)
    tree.insert(82)

    seen = DFS_InOrder(tree)
    print([node.value for node in seen])


if __name__ == '__main__':
    main()

