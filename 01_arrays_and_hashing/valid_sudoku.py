import collections
def is_valid_sudoku(board) -> bool:
    #This is not so much an array problem
    #but more of an... "efficiency/good practice coding" problem
    #the question itself is pretty straightforward
    #the real challenge is writing the code in the least amount of lines possible
    #while still being readable

    #subsquares
    #[[0, 1, 2], [3, 4, 5], [6, 7, 8]], each triplet belong to a subsquare
    #[    0          1           2   ], which can be represented by INTEGER DIVISION (//)
    #create a hash map/set with key being a tuple, each element indicating the index of square

    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    subsquares = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            #checking/updating row/col/square info at once
            #at the cost of more space
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in subsquares[(r // 3, c // 3)]):
                return False
            
            else:
                #update each hash
                rows[r].add(board[r][c])
                cols[r].add(board[r][c])
                subsquares[((r // 3, c // 3))].add(board[r][c])
    
    return True

def main():
    pass

if __name__ == "__main__":
    main()
