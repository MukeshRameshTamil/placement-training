class Solution(object):
    def setZeroes(self, matrix):
      
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
