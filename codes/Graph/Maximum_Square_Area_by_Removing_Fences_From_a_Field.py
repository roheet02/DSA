class Solution:
    def maximizeSquareArea(self, m, n, hFences, vFences):
        # Add the boundary fences for horizontal and vertical directions
        # 1 represents the start, m/n represents the end
        hFences.extend([1, m])
        vFences.extend([1, n])

        # Set to store all possible horizontal distances between fences
        stt = set()

        # Variable to store the maximum possible square side length
        ans = 0

        # Compute all possible distances between horizontal fences
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                # Absolute difference gives the height of a possible square
                stt.add(abs(hFences[j] - hFences[i]))

        # Compute all possible distances between vertical fences
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                # Absolute difference gives the width of a possible square
                val = abs(vFences[j] - vFences[i])

                # If this width exists as a height, a square is possible
                if val in stt:
                    # Update the maximum square side length
                    ans = max(ans, val)

        # If no square can be formed, return -1
        if ans == 0:
            return -1

        # Return the area of the largest square modulo 10^9 + 7
        return (ans * ans) % (10**9 + 7)
print(Solution().maximizeSquareArea(4,3,[2,3],[2]))