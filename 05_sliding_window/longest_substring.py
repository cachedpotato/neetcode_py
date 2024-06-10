def longest_substring_without_duplicates(strs: str) -> int:
    res = 0
    cset = set()
    #initialize l, r at the same point
    #r will keep moving down the string
    #add characters into a set, which will only contain unique characters

    #if r reaches a character already in the set, start moving l
    #l stops moving when l reaches the duplicate character
    l = r = 0
    while r < len(strs):
        #moving l
        while l < r and strs[r] in cset:
            cset.remove(strs[l])
            l += 1
        
        #if right character is not in the set
        #keep moving
        cset.add(strs[r])
        res = max(res, r - l + 1) #r = l: 1 char > length 1
        r += 1

    return res

def main():
    strs = "zxyzxyz"
    print("length of longest substring: {}".format(longest_substring_without_duplicates(strs)))
    strs = "xxxx"
    print("length of longest substring: {}".format(longest_substring_without_duplicates(strs)))

if __name__ == "__main__":
    main()
    