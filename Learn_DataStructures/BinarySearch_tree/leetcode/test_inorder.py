def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    if(tree == None):
        return
    
    iterativeInOrderTraversal(tree.left,callback)
    callback(tree)
    iterativeInOrderTraversal(tree.right,callback)