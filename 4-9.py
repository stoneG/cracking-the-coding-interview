from binary_tree import Node

def path_sum(root, num, path=[]):
    if sum(path) + root.value == num:
        print path + [root.value]
    if root.left:
        path_sum(root.left, num, path+[root.value])
    if root.right:
        path_sum(root.right, num, path+[root.value])

if __name__ == '__main__':
    root = Node(1)
    root.left, root.right = Node(2), Node(1)
    root.left.left, root.left.right = Node(1), Node(0)
    root.right.left, root.right.right = Node(1), Node(3)
    print """
    root =
          1
        2   1
       1 0 1 3
    """
    print 'now running path_sum(root, 3)'
    path_sum(root, 3)
