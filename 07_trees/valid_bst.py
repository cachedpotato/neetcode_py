from collections import deque
from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #THE ENTIRE SUBTREE HAS TO BE BIGGER OR SMALLER

    #start with -inf < root val < inf
    #for the left side: keep updating the left side of the boundary
    #-inf < left < root 
    #vice versa for right:
    #root < right < inf

    #if false: return false
    #if true: recursively keep checking
    def valid(node: Optional[TreeNode], left_boundary: int, right_boundary: int) -> bool:
      if not node:
        return True
      if (node.val >= right_boundary or node.val <= left_boundary):
        return False
      
      return (valid(node.left, left_boundary, node.val) and
                valid(node.right, node.val, right_boundary))
    
    return valid(root, -float("inf"), float("inf")) 
