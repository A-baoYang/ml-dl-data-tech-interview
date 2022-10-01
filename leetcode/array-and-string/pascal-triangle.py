from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(1, numRows + 1)]
        for row in range(2, numRows):
            for col in range(1, row):
                res[row][col] = res[row - 1][col - 1] + res[row - 1][col]
        return res

    def getRow(self, rowIndex: int) -> List[int]:
        row = [0] * (rowIndex + 1)
        for i in range(0, rowIndex + 1):
            for j in range(i, -1, -1):
                if j == 0 or j == i:
                    row[j] = 1
                else:
                    row[j] = row[j] + row[j - 1]
        return row
