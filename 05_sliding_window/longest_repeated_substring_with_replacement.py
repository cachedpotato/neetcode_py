def character_replacement(s: str, k: int) -> int:
    #we can change ANY character into ANY OTHER character
    #as long as our number of replacement is smaller or equal to k
    #what then, makes a certain substring "valid"?

    #a valid string of size l will always have non-most-frequent characters
    #smaller or equal to the replacement limit k
    #in other words: (r - l + 1) - max(count.values()) <= k
    #if not valid, we start moving the left pointer upwards until
    #the substring becomes valid again
    res = 0
    count = {}
    l = 0
    for r in range(len(s)):
        #update count
        count[s[r]] = count.get(s[r], 0) + 1

        #coding practice I should implement
        #It's normally a lot cleaner to write exception cases first
        #as it often times gets rid of unnecessary nesting


        #if not valid, move l until it becomes valid again
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        
        #if valid, keep moving
        res = max(res, r - l + 1)

    return res

def character_replacement_optimized(s: str, k: int) -> int:
    res = 0
    maxf = 0
    l = 0
    count = {}
    for r in range(len(s)): 
        #instead of computing the max value of count every single time,
        #we create a new variable maxf, which tracks the frequency of the most frequent characters
        #and use that for testing validity.
        
        #maxf is either
        #1) the current maxf value, or
        #2) the frequency of the current character, as we're going from left to right

        #the return value using this method will always be the length of the substring at the end

        count[s[r]] = count.get(s[r], 0) + 1

        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        
        res = max(res, (r - l + 1))
        
    return res 

def main():
    s = "AAABABB"
    k = 1
    print(character_replacement(s, k))
    print(character_replacement_optimized(s, k))

if __name__ == "__main__":
    main()