class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns: List[List[str]] = (
            [
                set() for _ in range(9)
            ])
        sections: List[List[str]] = (
            [
                set() for _ in range(9)
            ])
        rows: List[List[str]] = (
            [
                set() for _ in range(9)
            ])
        for row in range(9):
            for col in range(9):
                board_val = board[row][col]
                if board_val == ".":
                    continue

                num: int = board_val

                section = (row // 3) * 3 + (col // 3)
                if num in rows[row]:
                    return False
                if num in columns[col]:
                    return False
                if num in sections[section]:
                    return False

                rows[row].add(num)
                columns[col].add(num)
                sections[section].add(num)
        return True

                