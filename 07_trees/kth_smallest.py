
from typing import Optional
class TreeNode:
  def __init__(self, val=0, left=None, right=None) -> None:
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #kth smallest element in a valid BST
    #using dfs, go through all nodes from left>mid>right (forgot which order)
    #the list will be ordered
    #return kth element

    orderedList = []
    def dfs(node: Optional[TreeNode]) -> None:
      if not node:
        return
      #left > mid (curr) > right
      if node.left:
        dfs(node.left)
      
      #reached leaf node: add then return
      if not node.left and not node.right:
        orderedList.append(node.val)
        return
      
      #append mid(current)
      orderedList.append(node.val)

      #go right
      if node.right:
        dfs(node.right)
      
      return
    
    dfs(root)
    return orderedList[k - 1]
  
  def kthSmallestEfficient(self, root: Optional[TreeNode], k:int) -> int:
    #can we do this without having a separate list
    #and return as soon as we reach k?
    #iterative dfs with stacks might do the trick
  

    #The key here is that the stack itself is not in-order
    #but THE ORDER IN WHICH WE POP THE STACK is
    #whenever we traverse a node: append and move left
    #at leftmost node: pop and process
    # if right exists: move current to right

    n = 0
    stack = []
    curr = root
    while curr and stack:

      #step 1. traverse left
      while curr:
        stack.append(curr)
        curr = curr.left
      
      #step 2. in order - pop then process
      curr = stack.pop()
      n += 1
      if n == k:
        return curr.val
      
      #step 3. move right
      curr = curr.right


