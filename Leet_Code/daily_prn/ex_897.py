# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode):
        res = []
        self.helper_inOrder(root,res)
        root = TreeNode()
        root.val = res[0]
        cur = root
        for i in range(1,len(res)):
            newNode = TreeNode()
            newNode.val = res[i]
            cur.right = newNode 
            cur = cur.right
        return root
    def helper_inOrder(self,root:TreeNode,res:list[TreeNode]):
        if(root == None):
            return
        self.helper_inOrder(root.left,res)
        res.append(root.val)
        self.helper_inOrder(root.right,res)
