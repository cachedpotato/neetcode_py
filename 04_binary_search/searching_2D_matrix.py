def search_matrix(target, matrix) -> bool:
    #matrix is sorted
    #binary search 2 times: one for which row the target should be located
    #one for actually finding where the target is

    #get rid of edge cases immediately (O(1) time)
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False
    
    #Step 1. Row Binary Search
    in_row = 0
    l, r = 0, len(matrix)
    while l <= r:
        split = l + (r - l) // 2
        if matrix[split][0] < target:
            #lowermost boundary of the position
            #it may be in l, just not at the first element
            in_row = l
            l = split + 1
        elif matrix[split][0] > target:
            #uppermost boundary of the position
            #might be in the row right before split
            r = split - 1
            in_row = r
        
        else:
            #lucky!
            return True
    

    #Step 2. Trad. Binary Search
    l = 0
    r = len(matrix[0]) - 1 #just picked 0 for convenience
    while l <= r:
        split = l + (r - l) // 2
        if matrix[in_row][split] < target:
            l = split + 1
        elif matrix[in_row][split] > target:
            r = split - 1
        else:
            return True
    
    return False

def main():
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10
    print("target is in matrix: {}".format(search_matrix(target, matrix)))

if __name__ == "__main__":
    main()

    
            