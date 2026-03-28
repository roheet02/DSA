class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        s = [''] * n
        id = -1
        # Step 1: Greedy grouping
        for i in range(n):
            if s[i] != '':
                continue
            id += 1
            if id >= 26:
                return ""
            ch = chr(ord('a') + id)
            for j in range(n):
                if lcp[i][j] > 0:
                    s[j] = ch
        # Step 2: Validation
        for i in range(n):
            # Diagonal check
            if lcp[i][i] != n - i:
                return ""

            for j in range(i):
                x = lcp[i][j]

                # Symmetry check
                if x != lcp[j][i]:
                    return ""

                # LCP recurrence validation
                if s[i] == s[j]:
                    if i + 1 < n and j + 1 < n:
                        y = 1 + lcp[i + 1][j + 1]
                    else:
                        y = 1
                else:
                    y = 0

                if x != y:
                    return ""

        return "".join(s)

print(Solution().findTheString([[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]))