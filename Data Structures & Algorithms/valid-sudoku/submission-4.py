class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cells = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue
                
                cell = 3 * (row // 3) + col // 3
                if (val in rows[row]) or (val in cols[col]) or (val in cells[cell]):
                    return False
                rows[row].add(val)
                cols[col].add(val)
                cells[cell].add(val)

        return True