from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    #DFS Recursive Algorithm

    #Base case
    if not root:
      return 0
    
    #Base Logic
    #DFS - Starting on this node as root
    #Get the max depth of left and right
    #return that + 1 (current node)
    return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))