Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)
        return self.bstFromPreorderandInorder(preorder,inorder)
        
    def bstFromPreorderandInorder(self, preorder, inorder):
        lenthpre = len(preorder)
        lengthin = len(inorder)

        if lengthpre != lengthin or preorder == None or inorder == None or lenthpre == 0:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)

        root.left = self.bstFromPreorderandInorder(preorder[1:rootindex + 1],inorder[:rootindex])
        root.right = self.bstFromPreorderandInorder(preorder[rootindex + 1:],inorder[rootindex + 1:])
        return root

        