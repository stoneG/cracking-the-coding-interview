class Node(object):
    def __init__(self, adjacent_nodes=[]):
        self.visited = False
        self.adjacent = adjacent_nodes

def build_children(tree):
    children = []
    for node in tree:
        if isinstance(node, list):
            children.append(Node(build_children(node)))
        else:
            children.append(Node())
    return children

def build_tree(tree):
    return Node(build_children(tree))

if __name__ == '__main__':
    a = [1]*10
    b = [[1, 2, [3, 4, 5]], 1, [2, [3], 2]]
    print build_tree(a)
    print build_tree(b)
