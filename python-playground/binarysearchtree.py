#hi

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            root = node(data)
            return root
        else:
            if root.data <= data:
                root.right = self.insert(root.right, data)
            else:
                root.left = self.insert(root.left, data)
            return root

    
    def inorder_traversal(self, root):
        if not root:
            return
        if root.left:
            self.inorder_traversal(root.left)
        print(root.data)
        if root.right:
            self.inorder_traversal(root.right)
        return


if __name__ == '__main__':
    tree = bst()
    root = None
    for i in range(10):
        root = tree.insert(root, i)
    tree.inorder_traversal(root)