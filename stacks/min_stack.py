class MinStack:
  def __init__(self) -> None:
    self.stack = []
    self.min = []

  def push(self, val: int) -> None:
    self.stack.append(val)

    #push the current min value to the min stack
    if len(self.min) == 0: self.min.append(val)
    else:
      self.min.append(min(val, self.min[-1]))

  def pop(self) -> int:
    a = self.stack.pop()

    #pop the current min value as well
    self.min.pop()

    return a

  def top(self) -> int:
    return self.stack[-1]
    

  def getMin(self) -> int:
    return self.min[-1]


def main():
  minStack = MinStack()
  minStack.push(1)
  minStack.push(2)
  minStack.push(0)
  print("current stack: {}".format(minStack.stack))
  print("current min: {}".format(minStack.getMin()))
  minStack.pop()
  print("at top: {}".format(minStack.top()))
  print("current min: {}".format(minStack.getMin()))

if __name__ == "__main__":
  main()


