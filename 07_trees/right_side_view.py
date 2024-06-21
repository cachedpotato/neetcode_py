from typing import Optional
from collections import deque

class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def rightSideView(self, root: Optional[TreeNode]):
    if not root: return []

    #ONLY THE RIGHTMOST NODE VALUE PER LEVEL
    #LEVEL ORDER TRAVERSAL > ADD THE RIGHTMODE NODE VALUE ONLY
    #TO RESULT
    res = []

    q = deque()
    q.append(root)

    while q:
      level = []
      for _ in range(len(q)):
        n = q.popleft()
        level.append(n.val)

        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
      
      #We only need the rightmost node value
      res.append(level[-1])
    
    return res
  
  def rightSideViewEfficient(self, root: Optional[TreeNode]):
    #Instead of creaing an entire list
    #Keep track of just one (rightmost) node
    if not root:
      return []
    
    res = []
    q = deque()
    q.append(root)
    while q:
      right_most_node = None
      for _ in range(len(q)):
        n = q.popleft
        right_most_node = n
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
      
      res.append(right_most_node.val)
    
    return res
