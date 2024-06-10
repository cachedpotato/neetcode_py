def min_eating_speed(piles, h) -> int:
    #because we can't move to a different pile even if we finish one pile in a given hour,
    #the range of the speed we want will:
    #1. always be bigger than 0 (duh)
    #2. always be smaller or equal to the max number of bananas in a pile

    #k will be in a given RANGE 0 < k < max(piles)
    #RANGE can be thought of as a SORTED ARRAY
    #Sorted Array + fining target? Binary Search!

    max_speed = max(piles)
    l = 1
    r = max_speed
    res = max_speed
    while l <= r:
        split = l + (r - l) // 2
        hours_taken = 0
        for p in piles:
            if p % split == 0:
                hours_taken += p // split
            else:
                hours_taken += p // split + 1
        
        if hours_taken > h:
            #too slow
            l = split + 1
        else:
            #because of the // operation, we don't need a separate arm for exact matches
            #the speed value we want might not be "slow" enough for us for that to happen
            #If we get a faster speed, update the result first
            res = min(res, split)
            r = split - 1
        
    return res

def main():
    piles = [1, 4, 3, 2]
    h = 9
    ans = min_eating_speed(piles, h)
    print(ans)

    piles = [25,10,23,4]
    h = 4
    print(min_eating_speed(piles, h))


if __name__ == "__main__":
    main()