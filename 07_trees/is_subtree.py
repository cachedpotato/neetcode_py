from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #First, we need some function that checks if the trees are idential
    def isIdentical(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if not p and not q:
        return True
      
      if ((p and q) and (p.val == q.val)):
        return isIdentical(p.left, q.left) and isIdentical(p.right, q.right)
      else:
        return False
      

    #Logic:
    #First: "Filter" By subRoot
    if not subRoot:
      return not root

    if not root:
      return False
    else:
      #subRoot always there
      if not isIdentical(root, subRoot):
        #check if EITHER of the left/right side contain subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
      else:
        return True

