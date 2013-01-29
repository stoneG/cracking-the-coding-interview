from binary_tree import Node

def is_bst(root, min=float('-inf'), max=float('inf')):
    left, right, value = root.left, root.right, root.value
    if min < value < max:
        if left and right:
            return is_bst(left, min, value) and is_bst(right, value, max)
        elif left:
            return is_bst(left, min, value)
        elif right:
            return is_bst(right, value, max)
        return True
    return False

"""
BST
      4
   2     6
 1   3 5   7

BT
      4
   2     6
 1   8 5   7
"""

if __name__ == '__main__':
    bst = Node(4)
    bst.left, bst.right = Node(2), Node(6)
    bst.left.left, bst.left.right = Node(1), Node(3)
    bst.right.left, bst.right.right = Node(5), Node(7)
    bt = Node(4)
    bt.left, bt.right = Node(2), Node(6)
    bt.left.left, bt.left.right = Node(1), Node(8)
    bt.right.left, bt.right.right = Node(5), Node(7)
    print 'is_bst(bst) =', is_bst(bst)
    print 'is_bst(bt) =', is_bst(bt)
