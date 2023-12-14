class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        newNode = RBNode(val)
        newNode.left = self.nil 
        newNode.right = self.nil 
        newNode.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if newNode.val < current.val:
                current = current.left
            elif newNode.val > current.val:
                current = current.right
            else:
                return

        if parent == None:
            self.root = newNode
        else:
            newNode.parent = parent
            if newNode.val > parent.val:
                parent.right = newNode
            if newNode.val < parent.val:
                parent.left = newNode