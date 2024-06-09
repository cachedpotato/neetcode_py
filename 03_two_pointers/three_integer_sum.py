def three_sum(nums):
    nums.sort()
    res = []

    for i, n in enumerate(nums):
        #move to next different number
        if i > 0 and nums[i - 1] == n:
            continue

        #twosum 2 with j and k
        j, k = i + 1, len(nums) - 1
        while j < k:
            tsum = n + nums[j] + nums[k]
            if tsum < 0:
                j += 1
            elif tsum > 0:
                k -= 1
            else:
                res.append([n, nums[j], nums[k]])
                #update j to new value
                j += 1
                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return res
        

def main():
    nums = [-2, 0, 1, 1, 2]
    print("".join(f'{l}' for l in three_sum(nums)))

if __name__ == "__main__":
    main()




