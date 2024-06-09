def group_anagrams(strs):
    #the key of group anagrams is that
    #unlike regular valid anagrams problem where we only need to chekc
    #if the hashmaps are the same, we need to GROUP the hashes
    
    #another key is noticing that
    #instead of hashmaps, since we only use alphabets
    #we can create an array of size 26 which we can then both
    #store frequency AND use that as the key for the bigger hashmap

    freq_hash = {}
    for word in strs:
        #create count array
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        
        #update hash
        #arrays aren't hashable
        #but tuples are
        if freq_hash.get(tuple(count)) == None:
            freq_hash[tuple(count)] = [word]
        else:
            freq_hash[tuple(count)].append(word)
    
    return [l for l in freq_hash.values()]

def main():
    strs = ["act","pots","tops","cat","stop","hat"]
    l = group_anagrams(strs)
    print("".join(f'{c} ' for c in l))

if __name__ == "__main__":
    main()
    

    