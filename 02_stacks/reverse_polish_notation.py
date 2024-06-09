def evalRPN(token) -> int:
  operator = ["+", "-", "*", "/"]
  stack = []
  i = 0
  while i < len(token):
    while token[i] not in operator:
      stack.append(int(token[i]))
      i += 1

    a = stack.pop()
    b = stack.pop()
    match token[i]:
      case "+": stack.append(b + a)
      case "-": stack.append(b - a)
      case "*": stack.append(b * a)
      case "/": stack.append(b / a)
    
    i += 1
  
  return stack[0]

def main():
  tokens = ["4", "13", "5", "/", "+"]
  print("out: {}".format(evalRPN(tokens)))

if __name__ == "__main__": 
  main()