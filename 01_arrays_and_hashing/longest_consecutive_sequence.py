def longest_sequence(nums) -> int:
    #a sequence has a start and an end - how can we define these two?
    #start: there is no value smaller than it
    #end: there is no value that is one bigger than the one before

    res = 0
    num_set = set(nums)

    for n in num_set:
        if n - 1 in num_set:
            continue

        #sequences start found
        #get length of sequence
        length = 1
        while n + 1 in num_set:
            length += 1
            n += 1
        
        res = max(res, length)
            

    return res

def main():
    nums = [0,3,2,5,4,6,1,1]
    print(longest_sequence(nums))
    nums = [2,20,4,10,3,4,5]
    print(longest_sequence(nums))


if __name__ == "__main__":
    main()