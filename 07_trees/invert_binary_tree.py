from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right
  

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #Most Binary Tree Questions can be solved with recursions
    #Recursion
    #Base Case - Almost ALways Leaf Node (return null type beat)
    #Always consider the current node to be root

    #base case 
    if not root:
      return None
  
    #Base logic: Swap left and right
    root.left, root.right = root.right, root.left

    #recursion: do for all child nodes
    self.invertTree(root.left)
    self.invertTree(root.right)

    return root