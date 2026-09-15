class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def _getSection(r: int, c: int) -> int:
            if r < 3:
                if c < 3: return 0
                if c < 6: return 1
                return 2
            if r < 6:
                if c < 3: return 3
                if c < 6: return 4
                return 5
            if c < 3: return 6
            if c < 6: return 7
            return 8

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

                section = _getSection(row, col)
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

                