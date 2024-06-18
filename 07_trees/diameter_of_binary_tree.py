from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #Becase of how the diameter is defined,
    #we need to approach from the BOTTOM UP
    #instead of TOP DOWN

    #BOTTOM UP methods normally require helper functions
    #Whereas TOP DOWN approach need recursion of our solution function itself

    #starting from the bottom, base case
    
    if not root:
      return 0
    
    #helper function require global variable
    res = [0]

    def helper(node: Optional[TreeNode]) -> int:
      #do a DFS search for left and right
      #grab the max depth

      #we are returning -1 because we need to ADD both max(left) and max(right)
      #the formula we're trying to use
      #2 + max_l + max_r
      #for this to accomodate None type nodes: we need to return -1

      if not node: 
        return -1

      #update the diameter using the formula
      res[0] = max(res[0], 2 + helper(node.left) + helper(node.right))
      
      #return depth to go up
      return 1 + max(helper(node.left), helper(node.right))
    


    return res[0]