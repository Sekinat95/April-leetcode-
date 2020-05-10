# Given a binary tree, you need to compute the 
# length of the diameter of the tree. The diameter of a binary tree 
# is the length of the longest path between any two nodes in a tree. 
# This path may or may not pass through the root.
    #       1
    #      / \
    #     2   3
    #    / \     
    #   4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# Note: The length of path between two nodes is represented by the number of edges between them.
def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0;
    lheight = self.height(root.left)
    rheight = self.height(root.right)

    ldiameter = self.diameterOfBinaryTree(root.left)
    rdiameter = self.diameterOfBinaryTree(root.right)

    return max(lheight + rheight, max(ldiameter,rdiameter))

    
def height(self, root):
    if root is None:
        return 0;
    else:
        return 1 + max(self.height(root.left),self.height(root.right))