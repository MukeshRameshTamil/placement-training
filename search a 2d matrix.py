class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        index = -1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left = 0
                right = len(matrix[mid]) - 1
                index = mid
                break
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        if index == -1:
            return False
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        r```Explanation []eturn False
