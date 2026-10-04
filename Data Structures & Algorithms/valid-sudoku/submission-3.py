class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cells = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if board[i][j] == ".":
                    continue
                
                row = i
                col = j
                cell = 3 * (i // 3) + j // 3
                if (val in rows[row]) or (val in cols[col]) or (val in cells[cell]):
                    return False
                rows[row].add(val)
                cols[col].add(val)
                cells[cell].add(val)

        return True