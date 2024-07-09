from typing import Optional
#GRAPH: ALWAYS HAVE VISITED SET
#UNLIKE BST GRAPHS ARE "DOUBLY LINKED"
#IN CASE OF RECURSION: MAY END UP IN INFINITE LOOP

class Node:
  def __init__(self, val = 0, neighbors = None) -> None:
    self.val = val
    self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional[Node]) -> Optional[Node]:
  if not node: return None

  #just like the BT Cloning problem, use hashmap
  #then add connections later
  #ALSO MAKE VISITED SET
  nodeMap = {}
  visited = set()

  def dfs(node: Optional[Node]) -> None:
    if not node:
      return
    
    nodeMap[node] = Node(node.val, [])
    for n in node.neighbors:
      if n not in visited:
        visited.add(n)
        dfs(n)
    
    return
  
  dfs(node)
  root = nodeMap[node]

  #adding connections
  for oldNode, newNode in nodeMap.items():
    for n in oldNode.neighbors:
      newNode.neighbors.append(nodeMap[n])
  
  return root


