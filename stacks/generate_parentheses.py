def generate_parentheses(n: int):
  #Key: Parentheses: possibly stack
  #Looks like I need some sort of tree finding > recursion

  #tree recursion
  #Stack as a means of getting solution and traversing up the tree via pop
  #just like BFS, DFS, etc

  #Figure out when we can input what
  #iff open > closed: input ) possible
  #if open < n: ) possible
  # if open == closed == n: one solution found

  res = []
  par_stack = []

  def backtrack(num_open, num_closed):
    #base case
    if num_open == num_closed == n:
      res.append("".join(par_stack))
      return
    
    #arm 1
    if num_open < n:
      par_stack.append("(")
      backtrack(num_open + 1, num_closed)
      par_stack.pop() #once done, travers UP the tree via pop

    #arm 2
    if num_open > num_closed:
      par_stack.append(")")
      backtrack(num_open, num_closed + 1)
      par_stack.pop()
    
  backtrack(0, 0)
  return res

def main():
  n = 5
  print("".join(f'{s} ' for s in generate_parentheses(n)))

if __name__ == "__main__":
  main()