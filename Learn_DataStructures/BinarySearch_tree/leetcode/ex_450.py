#Ex 450 Delete Node in a BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if(root == None):
            return root
        
        if(key < root.val):
            root.left = self.deleteNode(root.left,key)
        elif(key > root.val):
            root.right = self.deleteNode(root.right,key)
        
        else:
            #node to be deleted have one child or no children
            if(root.left == None and root.right == None):
                root = None
            
            elif(root.left == None):
                temp = root.right
                root.right = None
                root = temp
            elif(root.right == None):
                temp = root.left
                root.left = None
                root = temp
            
            #node to be deleted have 2 children
            elif(root.left != None and root.right != None):
                temp_data = self.get_MinVal(root.right)
                root.val = temp_data.val
                root.right=self.deleteNode(root.right,temp_data.val)

        return root

    def get_MinVal(self,root : TreeNode):
        cur = root 
        while(cur.left != None):
            cur = cur.left
        return cur    