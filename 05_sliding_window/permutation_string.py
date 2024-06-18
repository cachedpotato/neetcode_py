def permutation_string(s1: str, s2: str) -> bool:
    #we need to find permutations of s1 INSIDE s2
    #permutations are just a fancier word for anagrams
    #HASH MAP BABY
    #if in s2, we encounter a character in s1's count hash:
    #get the count info if substring starting from that character, of length len(s1)
    #if count info is the same, then return true
    #if not, keep moving

    #if s1 > s2: we don't even need to check
    if len(s1) > len(s2): return False

    count = {}
    for c in s1:
        count[c] = count.get(c, 0) + 1

    for i in range(len(s2)):
        if count.get(s2[i]) == None:
            continue
        
        bigcount = {}
        for j in range(i, len(s1) + i):
            #if j reaches the end before finishing, it's not a permutation
            if j >= len(s2): return False
            bigcount[s2[j]] = bigcount.get(s2[j], 0) + 1

        #if two count data is the same, we found the permutation
        if count == bigcount: return True

    return False

#TODO
def permutation_string_optimized(s1: str, s2: str) -> bool:
    return False

def main():
    s1 = "abc"
    s2 = "a;lskdjfaoiscabAskasjkdfl"
    print("the statement 'there exists a permutation of s1 in s2' is: {}".format(permutation_string(s1, s2)))

if __name__ == "__main__":
    main()