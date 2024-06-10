def two_sum_2(nums, target):
    #similar to two sum, but the list is sorted
    #because the list is pre-sorted, we can just use two pointers, starting at both ends
    #if the sum is big > move right pointer down
    #if sum is small > move left pointer up
    l, r = 0, len(nums) - 1
    while l < r: #no overlapping allowed
        if target < nums[l] + nums[r]:
            r -= 1
        elif target > nums[l] + nums[r]:
            l += 1
        else:
            return [l, r]

    return []

def main():
    nums = [0, 1, 3, 5, 9]
    target = 6
    print(two_sum_2(nums, target))

if __name__ == "__main__":
    main()