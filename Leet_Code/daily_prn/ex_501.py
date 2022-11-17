class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root : TreeNode) :
        res = []
        data = {}
        self.getData(root,data)
        maxCount = max(list(data.values()))
        for item in data:
            if(data[item]==maxCount):
                res.append(item)
        return res

    def getData(self,root : TreeNode,data : dict):
        if(root == None):
            return
        if(root.val not in data):
            data[root.val]=1
        else:
            data[root.val]+=1
        self.getData(root.left,data)
        self.getData(root.right,data)