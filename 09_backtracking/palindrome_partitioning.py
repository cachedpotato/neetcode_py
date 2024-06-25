def partition(s: str):
    if len(s) == 0: return []

    res = []
    l = len(s)

    def isPalindrome(subString: str) -> bool:
        if len(subString) <= 1: return True
        for i in range(len(subString) // 2):
            if subString[i] == subString[len(subString) - 1 - i]:
                continue
            else:
                return False
        
        return True
    
    def backtrack(subStringList, idx):
        nonlocal l
        nonlocal s
        if idx >= l: 
            res.append(subStringList.copy())
            return
        
        i = idx + 1
        while i <= l:
            if isPalindrome(s[idx:i]):
                subStringList.append(s[idx:i])
                print(subStringList)
                backtrack(subStringList, i)
                subStringList.pop()
            
            i += 1
    
    backtrack([], 0)
    return res

def main():
    s = "aab"
    res = partition(s)
    for l in res:
        print(l)

if __name__ == "__main__":
    main()
