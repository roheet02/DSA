class Solution:
    def minimumDeleteSum(self, s1, s2):
        # m and n are lengths of both strings
        m, n = len(s1), len(s2)
        # dp[i][j] will store the maximum ascii sum of common subsequence
        # between s1[i:] and s2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # filling dp table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # if characters match, take ascii value and move diagonally
                if s1[i] == s2[j]:
                    dp[i][j] = ord(s1[i]) + dp[i + 1][j + 1]
                # if not matching, skip one character from either string
                # and take the better option
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        # total ascii sum of both strings
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        # subtract twice the common ascii sum to get minimum delete sum
        return total - 2 * dp[0][0]
print(Solution().minimumDeleteSum("sea", "eat"))
