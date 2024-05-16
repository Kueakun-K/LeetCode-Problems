class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(self, root):
    if not root.left and not root.right:
        if root.val == 0:
            return False
        return True
    left = self.evaluateTree(root.left)
    right = self.evaluateTree(root.right)
    if root.val == 2:
        return left or right
    return left and right 

root = TreeNode([2,1,3,None,None,0,1])