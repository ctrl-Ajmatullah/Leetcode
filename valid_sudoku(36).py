"""Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition."""

import collections
def isValidSudoku(board):
    rows_hash_set = collections.defaultdict(set)
    cols_hash_set = collections.defaultdict(set)
    boxes_hash_set = collections.defaultdict(set)
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            
            if (board[r][c] in rows_hash_set[r] or
                board[r][c] in cols_hash_set[c] or
                board[r][c] in boxes_hash_set[(r//3,c//3)]):
                return False
            
            rows_hash_set[r].add(board[r][c])
            cols_hash_set[c].add(board[r][c])
            boxes_hash_set[(r//3,c//3)].add(board[r][c])
    return True

print(isValidSudoku(
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))
    
    