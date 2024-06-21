from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def constructBinaryTree(self, inorder, preorder) -> Optional[TreeNode]:
    #THE FIRST NODE IN PREORDER IS ROOT
    #INORDER: LEFT > MID > RIGHT

    #0---LEFT SUBTREE-------SPLIT------RIGHT SUBTREE-----# FOR INORDER
    #ROOT=----LENGTH: SPLIT------NEWROOT ------------- --# FOR PREORDER
    root = TreeNode(preorder[0])
    split = inorder.index(preorder[0])

    root.left = self.constructBinaryTree(
      inorder[0:split], 
      preorder[1:split + 1]
    )
    root.right = self.constructBinaryTree(
      inorder[split + 1:], 
      preorder[split + 1:]
    )

    return root
