def search(nums, target) -> int:
    l = 0
    r = len(nums) - 1
    if nums[0] > nums[-1]:
        #rotated -> find minimum
        min_idx = (1001, 0)
        l, r = 0, len(nums) - 1
        while l < r:
            split = l + (r - l) // 2
            #update min
            if nums[split] < min_idx[0]:
                min_idx = (nums[split], split)
            
            
            if nums[split] > nums[r]:
                #min at right
                l = split + 1
            else:
                #min at left
                r = split - 1
        
        if nums[l] < nums[min_idx[1]]:
            min_idx = (nums[l], l)
        #we got the min index
        #find which side we're looking
        if target > nums[-1]:
            l = 0
            r = min_idx[1] - 1
        
        elif target < nums[-l]:
            l = min_idx[1]
            r = len(nums) - 1
        
        else:
            return len(nums) - 1
    
    #regular BSA
    while l <= r:
        split = l + (r - l) // 2
        if nums[split] < target:
            l = split + 1
        elif nums[split] > target:
            r = split - 1
        else:
            return split
    
    return -1

def search_optimized(nums, target) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        split = l + (r - l) // 2
        if nums[split] == target:
            return split
        if nums[l] <= nums[split]:
            #we are at the left sorted portion
            #if the target is bigger than leftmost, then we would need to search the left portion
            #if the target is smaller, then we would need to search the right sorted portion

            #target is within the left sorted portion, just a bit bigger
            if target > nums[split]:
                l = split + 1

            #target is actually at the right sorted portion
            #we need to move right
            elif target < nums[l]:
                l = split + 1
            
            else:
                r = split - 1

        else:
            #we are at the right sorted portion
            #if the target is bigger than the rightmost, then we need to search the left portion
            #if not, search the right sorted portion
            if nums[split] > target:
                #midpoint is past the target, make it smaller
                r = split - 1

            #cases where target is bigger than midpoint
            #1) target belongs to the left sorted portion
            #2) target belongs to the right sorted portion, just bigger
            elif target > nums[r]: #nums[r] is the biggest of the right sorted portion
                r = split - 1
            else:
                l = split + 1


    return -1







def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    a = search(nums, target)
    print(a)

if __name__ == "__main__":
    main()