class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1
        while low <= high:
            mid = (low + high) // 2
            mid_row = mid // cols
            mid_col = mid % cols
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False