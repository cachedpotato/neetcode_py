from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q:TreeNode):
    #BINARY SEARCH TREE
    #ALL VALUES UNIQUE

    #Iterative search
    #IF root < p, q: search right
    #IF p, q < root: search left
    #ELSE: return root (either p<root<q or q<root=p)

    while root:
      if (root.val < p.val and root.val < q.val):
        root = root.right
      elif (p.val < root.val and q.val < root.val):
        root = root.left
      else:
        return root