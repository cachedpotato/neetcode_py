def find_min(nums) -> int:
    #if it's not been rotated len(list)*n times, the first element will always be bigger than the last
    #if not, then the first element will be the smallest
    if nums[0] < nums[-1]: return nums[0]

    #god damn this is hard
    #update: OH MY GOD I DID IT YESSSSSSSSSSS
    #nth rotation: the minmum value is at index n
    #can we use this fact?

    #in the case of overestimating AND the target (t <= split)
    #nums[split] < nums[0]
    #check if it's the target by checking nums[split] < nums[split - 1]
    #if not cut the window standard BS way

    #in the case of underestimating (t > split):
    #nums[split] > nums[0]
    
    l = 1
    r = len(nums)
    while l <= r:
        split = l + (r - l) // 2
        if nums[split] < nums[0]:
            #overestimation
            #rotation value lower
            #bring r down to split
            if nums[split] < nums[split - 1]:
                return nums[split]
            r = split - 1
        else:
            #underestimation
            #rotation value higher
            l = split + 1
    #unreachable
    return -1

def find_min_optimized(nums):
    #of course there is a simpler way of doing things
    #we can just keep updating the minimum values
    #and return the lower value of whatever that is
    #and the left side of the current range
    l, r = 0, len(nums) - 1
    current_min = 1001 #via constraint

    #we are NOT considering the case of l == r
    while l < r:
        split = l + (r - l) // 2
        current_min = min(current_min, nums[split])
        if nums[split] > nums[r]:
            #underestimation
            l = split + 1
        else:
            #overestimation
            r = split - 1
    
    return min(current_min, nums[l])


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(find_min(nums))
    print(find_min_optimized(nums))

if __name__ == "__main__":
    main()