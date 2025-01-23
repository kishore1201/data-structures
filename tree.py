class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data, parentdata=None):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
            return
        parentnode = self.find_node(parentdata, self.root)
        if not parentnode:
            print("Parent not found")
            return
        parentnode.children.append(node)

    def find_node(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            node_found = self.find_node(data, child)
            if node_found is not None:
                return node_found
        return None

    def display(self, depth=0, node=None):
        if node is None:
            node = self.root
        print(" " * depth, node.data)
        for child in node.children:
            self.display(depth + 1, child)

    def remove(self, data):
        if not self.root:
            print("Tree is empty")
            return
        if self.root.data == data:
            self.root = None
            return
        parentnode = self.findParentNode(data, self.root)
        if parentnode:
            for child in parentnode.children:
                if child.data == data:
                    parentnode.children.remove(child)
                    return
        print("Node not found")

    def findParentNode(self, data, node):
        for child in node.children:
            if child.data == data:
                return node
            node_found = self.findParentNode(data, child)
            if node_found is not None:
                return node_found
        return None

# Testing the Tree class
trees = Tree()
trees.add(1)
trees.add(2, 1)
trees.add(3, 1)
trees.add('a', 1)
trees.add(4, 2)
trees.add(5, 2)
trees.add(6, 3)
trees.add(7, 3)
trees.display()
trees.remove('a')
trees.display()
