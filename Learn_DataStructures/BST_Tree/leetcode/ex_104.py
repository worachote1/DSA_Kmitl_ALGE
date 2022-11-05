#Ex 104 Maximum Depth of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.helper(root)

    def helper(self, root,count=0) :
        if(root == None):
            return count-1
        
        maxLeft_depth = self.helper(root.left,count+1)
        maxRight_depth = self.helper(root.right,count+1)
        return max(maxLeft_depth,maxRight_depth)