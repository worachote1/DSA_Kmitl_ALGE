class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) :
        res = []
        self.getSub(root,res,[])
        return self.cal(res)

    def getSub(self,root : TreeNode,res : list,sub_res : list):
        if(root==None):
            return
        sub_res.append(root.val)
        if(root.left == None and root.right == None):
            res.append(sub_res)
            return
        sub_left = sub_res.copy()
        sub_right = sub_res.copy()
        self.getSub(root.left,res,sub_left)
        self.getSub(root.right,res,sub_right)
        
    def cal(self,res : list):
        sumNum = 0
        for item in res:
            for k in range(len(item)):
                sumNum += item[k]*(2**(len(item)-1-k))
        return sumNum