from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #TOP DOWN approach
    #recursively check if the height of both sides are no more different
    #than 1

    #we need dfs for this, but first: base case:
    if not root:
      return True
    
    #helper dfs
    def dfs(node: Optional[TreeNode]) -> int:
      if not node:
        return 0
      return 1 + max(node.left, node.right)
    
    #if height difference bigger than 1 - return False immediately
    if (abs(dfs(root.left), dfs(root.right)) > 1):
      return False
    
    #if not - recursively check
    return self.isBalanced(root.left) and self.isBalanced(root.right)
    
