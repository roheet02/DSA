class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for n in nums:
            # For n == 2, the problem requires returning -1
            if n == 2:
                ans.append(-1)
                continue
            # (n + 1) & (-(n + 1))
            # This expression extracts the lowest set bit (LSB) of (n + 1)
            # Example:
            # n = 5  -> n + 1 = 6  -> binary: 110
            # LSB = 2
            lowest_set_bit = (n + 1) & (-(n + 1))
            # We subtract half of that lowest set bit from n
            # This ensures the resulting number produces the same
            # bitwise OR result with its pair as required by the problem
            result = n - (lowest_set_bit // 2)
            ans.append(result)
        return ans

# Example usage
print(Solution().minBitwiseArray([2, 3, 5, 7]))
