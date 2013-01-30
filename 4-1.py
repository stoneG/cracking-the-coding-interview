from tree_builder import *

def is_balanced(tree, counter=0):
    global depth
    if not tree.adjacent:
        if counter not in depth:
            depth.append(counter)
        if len(depth) > 2:
            return False
        else:
            return True
    left = tree.adjacent[0]
    right = tree.adjacent[1]
    return is_balanced(left, counter+1) and is_balanced(right, counter+1)

if __name__ == '__main__':
    unbalanced = build_tree([1, [1, [1, [1, 1]]]])
    balanced = build_tree([[[],[1,1]],[[],[1,1]]])
    depth = []
    print 'is_balanced(balanced) ->', is_balanced(balanced)
    depth = []
    print 'is_balanced(unbalanced) ->', is_balanced(unbalanced)
