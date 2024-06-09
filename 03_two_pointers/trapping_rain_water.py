def trap(height) -> int:
    res = 0
    #look things SIDEWAYS
    #iterate over y axis

    #per y level - get subtotal
    for h in range(1, max(height) + 1, 1):
        #get indeces of values in list higher than current height
        same_height_idx = []
        for i, a in enumerate(height):
            if a >= h:
                same_height_idx.append(i)
        
        sub_total = 0
        #get area of rain in a given height
        #which are sums of gaps between indeces
        for i in range(0, len(same_height_idx) - 1, 1):
            sub_total += same_height_idx[i + 1] - same_height_idx[i] - 1
        
        res += sub_total

    return res

def trap_two_pointer(height) -> int:
    #break down the problem into smaller examples
    #how do we calculate the amount of water storable in a given point?
    #min(maxh_l, maxh_r) - h[i], where maxh_l/r are the max heights of bars surrounding the given point
    #water can be stored IFF maxh_l/r > h[i] => ignore negatives
    res = 0
    l, r = 0, len(height) - 1
    maxh_l, maxh_r = height[l], height[r]
    
    #both edges cannot hold water
    while l < r:
        if maxh_l < maxh_r:
            l += 1
            maxh_l = max(maxh_l, height[l])
            #because we update the max height before getting the area,
            #the maxh_l will always be bigger or equal to current height
            #we can just add to res without checking if it's smaller than 0 (not necessary)
            res += maxh_l - height[l]
        else:
            r -= 1
            maxh_r = max(maxh_r, height[r])
            res += maxh_r - height[r]
        
    return res

def main():
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    r = trap_two_pointer(height)
    print(r)

if __name__ == "__main__":
    main()