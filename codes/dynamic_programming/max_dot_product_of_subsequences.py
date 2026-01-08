class Solution:
    def maxDotProduct(self,nums1,nums2):
        n, m = len(nums1), len(nums2)
        dp = [[None] * m for _ in range(n)]
        def solve(i, j):
            if i >= n or j >= m:
                return -10**9
            if dp[i][j] is not None:
                return dp[i][j]
            ans = -10**9
            ans = max(ans,nums1[i] * nums2[j] + max(0, solve(i + 1, j + 1)))
            ans = max(ans, solve(i + 1, j))
            ans = max(ans, solve(i, j + 1))
            dp[i][j] = ans
            return ans
        return solve(0, 0)
print(Solution().maxDotProduct([2,1,-2,5],[3,0,-6]))

        