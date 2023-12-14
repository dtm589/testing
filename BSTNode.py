class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
            
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


    def get_min(self):
        min = self
        while min.left != None:
            min = min.left
        return min.val

    def get_max(self):
        max = self
        while max.right != None:
            max = max.right
        return max.val
    
    def preorder(self, visited):
        visited.append(self.val)
        if self.left != None:
            self.left.preorder(visited)
        if self.right != None:
            self.right.preorder(visited)
        return visited