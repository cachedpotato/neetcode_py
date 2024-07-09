#topological sort
#traverse through the graph while checking for loops
#if no loop found & at the end (starting point), then
#add that to our path output and remove that node from graph
#this can be done using a separate set

from typing import List
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
  #course <- prerequisite relation
  prereq = {i: [] for i in range(numCourses)} 
  for crs, pre in prerequisites:
    prereq[crs].append(pre)

  clear = set() #for "removing" nodes from graph
  loopcheck = set() #for checking loops/cycles
  path = []

  def dfs(crs: int) -> bool:
    if crs in clear: 
      return True
    
    if crs in loopcheck:
      return False
    
    #main body
    loopcheck.add(crs)
    for pre in prereq[crs]:
      #check if there's loop going down the graph
      if not dfs(pre):
        return False
    
    #All good - remove from loopchecker
    #and add to clear set
    #also append to path
    loopcheck.remove(crs)
    clear.add(crs)
    path.append(crs)
    return True
  
  #go through all nodes to create full path
  for c in range(numCourses):
    if not dfs(c):
      return []
  
  return path


def main():
  numCourses = 5
  prerequisites = [[0,1], [1,2], [2,3], [1,4]]
  schedule = findOrder(numCourses, prerequisites)
  print(" ".join([f'{s}' for s in schedule]))

if __name__ == "__main__":
  main()