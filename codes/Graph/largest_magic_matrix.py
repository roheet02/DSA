class Solution:
    def largestMagicSquare(self, grid):
        rows, cols = len(grid), len(grid[0])
        ans = 1  # Minimum magic square size is always 1
        # Check if k x k square starting at (r, c) is a magic square
        def is_magic(r, c, k):
            target_sum = sum(grid[r][c:c + k])  # Sum of first row
            # Check all rows
            for i in range(r, r + k):
                if sum(grid[i][c:c + k]) != target_sum:
                    return False
            # Check all columns
            for j in range(c, c + k):
                if sum(grid[i][j] for i in range(r, r + k)) != target_sum:
                    return False
            # Check main diagonal
            if sum(grid[r + d][c + d] for d in range(k)) != target_sum:
                return False
            # Check anti-diagonal
            if sum(grid[r + d][c + k - 1 - d] for d in range(k)) != target_sum:
                return False
            return True
        # Try all possible square sizes
        for size in range(2, min(rows, cols) + 1):
            for r in range(rows - size + 1):
                for c in range(cols - size + 1):
                    if is_magic(r, c, size):
                        ans = size  # Update largest valid size found
        return ans
print(Solution().largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))
