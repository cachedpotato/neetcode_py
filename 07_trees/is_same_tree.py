from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    plist = []
    qlist = []

    #change p and q to list, like the example shown
    #check two lists if they are the same 

    #Top down means...?
    def toList(node: Optional[TreeNode], l):
      if not node:
        l.append(None)
        return
      
      l.append(node.val)
      toList(node.right, l)
      toList(node.left, l)


    toList(p, plist)
    toList(q, qlist)

    return plist == qlist
  
  def isSameTreeNoMemory(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #We used List above
    #can we do better?

    #TOP DOWN - BASE CASE
    if not p and not q:
      return True
    
    #Base Logic
    #check both left and right recursively
    #return false immediately if we see any difference
    
    #recursive checking: only when p and q exist and they share the same value
    #everything else: false

    if ((p and q) and (p.val == q.val)):
      #Recursively check both sides of the tree
      return self.isSameTreeNoMemory(p.left, q.left) and self.isSameTreeNoMemory(p.right, q.right)
    else:
      #Any other case is False
      return False


    