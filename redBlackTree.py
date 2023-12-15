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
                
        self.fix_insert(new_node)
                
                
        def rotate_left(self, x):
            if x == self.nil or x.right == self.nil:
                return
            y = x.right
            x.right = y.left

            if y.left != self.nil:
                y.left.parent = x
            y.parent = x.parent

            if x == self.root:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            elif x == x.parent.right:
                x.parent.right = y

            y.left = x
            x.parent = y
            

        def rotate_right(self, x):
            if x == self.nil or x.left == self.nil:
                return
            y = x.left
            x.left = y.right

            if y.right != self.nil:
                y.right.parent = x
            y.parent = x.parent

            if x == self.root:
                self.root = y
            elif x == x.parent.right:
                x.parent.right = y
            elif x == x.parent.left:
                x.parent.left = y

            y.right = x
            x.parent = y
            
    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red == True:
            if new_node.parent == new_node.parent.parent.right:
                uncle = new_node.parent.parent.left
                if uncle.red == True:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.right

                if uncle.red:
                    uncle.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False