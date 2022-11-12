class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        res = []
        self.helper(root,res,"")
        return res
    
    def helper(self,root : TreeNode,res : list,ss_data : str):
        if(root == None):
            return
        if(root.left == None and root.right == None):
            data = ss_data[:len(ss_data)]+str(root.val)
            res.append(data)
            return
        self.helper(root.left,res,ss_data+str(root.val)+"->")
        self.helper(root.right,res,ss_data+str(root.val)+"->")

