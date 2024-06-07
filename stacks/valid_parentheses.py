def is_valid_parentheses(s):
  #the crux of this question is that parentheses always comes in pairs
  #and the innermost pair is evaluated first
  #innermost > most recent > LIFO > STACK
  if len(s)%2 != 0: return False

  par_stack = []
  pairs = {')': '(', '}': '{', ']': '['} 
  for c in s:
    match c:
      case '(':
        par_stack.append(')')
      case '{':
        par_stack.append('}')
      case '[':
        par_stack.append(']')
      case ')' | '}' | ']' if len(par_stack) != 0:
        if c != par_stack.pop(): return False
      case _:
        return False
  
  #stack must be empty at the end
  if len(par_stack) == 0: return True
  return False

def main():
  test_case_1 = "()(){}{{}}"
  test_case_2 = "({[[(){}]]})(]"
  print("test_case_1: {}".format(is_valid_parentheses(test_case_1)))
  print("test_case_2: {}".format(is_valid_parentheses(test_case_2)))

if __name__ == "__main__":
  main()