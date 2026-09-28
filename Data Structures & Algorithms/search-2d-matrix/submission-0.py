class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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

# matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target=3
# low = 0
# high = 1
# mid = 0
# mid_row = 0
# mid_col = 0