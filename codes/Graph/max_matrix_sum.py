class Solution:
    def maxMatrixSum(self, matrix):
        total_sum = 0
        neg = 0
        min_abs = float('inf')

        for row in matrix:
            for v in row:
                if v < 0:
                    neg += 1
                av = abs(v)
                total_sum += av
                min_abs = min(min_abs, av)

        return total_sum if neg % 2 == 0 else total_sum - 2 * min_abs

print(Solution().maxMatrixSum([[1,-1],[-1,1]]))