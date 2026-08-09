class Solution(object):
    def spiralOrder(self, matrix):
        res = []

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:

            # top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
        