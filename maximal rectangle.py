class Solution(object):
    def maximalRectangle(self, matrix):
       
        if not matrix or not matrix[0]:
             return 0

        n = len(matrix[0])
        height = [0] * (n + 1)
        max_area = 0

        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
