def binary_search(target, nums) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        split = l + (r - l) // 2
        if nums[split] < target:
            l = split + 1
        elif nums[split] > target:
            r = split - 1
        else:
            return split
    
    return -1 

def main():
    nums = [0, 1, 3, 5, 9, 11, 13]
    target = 11
    print("at index {}".format(binary_search(target, nums)))

if __name__ == "__main__":
    main()

