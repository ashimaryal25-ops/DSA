class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                row_tuple = (r, "row", val)
                col_tuple = (c, "col", val)
                box_tuple = (r // 3, c // 3, "box", val)
                
                if row_tuple in seen or col_tuple in seen or box_tuple in seen:
                    return False
                
                seen.add(row_tuple)
                seen.add(col_tuple)
                seen.add(box_tuple)
                
        return True
        