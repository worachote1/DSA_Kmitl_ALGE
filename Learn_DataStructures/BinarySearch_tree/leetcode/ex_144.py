#144. Binary Tree Preorder Traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        res = []
        self.helper(root,res)
        return res

    def helper(self,root,res):
        if(root == None):
            return
        
        res.append(root.val)
        self.helper(root.left,res)
        self.helper(root.right,res)
