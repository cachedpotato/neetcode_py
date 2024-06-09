def max_area(heights) -> int:
    l = 0 
    r = len(heights) - 1
    res = (r - l)*min(heights[r], heights[l])

    #does not matter how much you move through the list while "skipping" some calculations
    #O(n) is still O(n) as long as you have to iterate through the entire list
    #why not make things simple then?
    while l < r:
        #keep things simple
        #just move stuff one by one
        #don't add any bloats
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
            #edge case where both heights are the same:
            #updating either of the height is okay
        
        #update max area
        res = max(res, (r - l)*min(heights[r], heights[l]))

    return res

def main():
    heights = [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
    heights1 = [1,7,2,5,4,7,3,6]
    heights2 = [2, 2, 2]

    print(max_area(heights))
    print(max_area(heights1))
    print(max_area(heights2))

    test = [8]
    for i in range(0, len(test) - 1, 1):
        print(test[i + 1])

if __name__ == "__main__":
    main()


            


    