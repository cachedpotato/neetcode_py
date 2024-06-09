def largest_rectangle(heights) -> int:
    res = 0
    #we going O(n * m) on this one idk I'm too dumb
    max_height = max(heights)
    for h in range(1, max_height + 1, 1):
        stack = []
        for i, a in enumerate(heights):
            if a >= h:
                if stack and stack[-1] + 1 < i:
                    res = max(res, len(stack)*h)
                    #reset stack and append current idx
                    stack = [i]
                else:
                    stack.append(i)
            res = max(res, len(stack) * h)
    
    return res

def largest_rectangle_improved(heights) -> int:
    res = 0

    return res

def main():
    heights = [7,1,7,2,2,4]
    print(largest_rectangle(heights))
    heights = [1,3,7]
    print(largest_rectangle(heights))


if __name__ == "__main__":
    main()