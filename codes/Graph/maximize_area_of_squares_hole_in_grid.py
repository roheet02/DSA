class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):

        # This function finds the maximum length of
        # consecutive bars (with difference = 1)
        def maxLen(Bars):
            count, length = 2, 2  
            # count  -> current consecutive length
            # length -> maximum consecutive length found so far

            # Traverse the bars list
            for i in range(1, len(Bars)):
                # If current bar and previous bar are consecutive
                if Bars[i] - Bars[i - 1] == 1:
                    count += 1
                else:
                    # Reset count if they are not consecutive
                    count = 2

                # Update the maximum length
                length = max(length, count)

            return length

        # Sort both horizontal and vertical bars
        hBars.sort()
        vBars.sort()

        # Find the maximum possible square side
        # It is limited by the minimum of horizontal and vertical lengths
        side = min(maxLen(hBars), maxLen(vBars))

        # Return the area of the square
        return side * side
      
print(Solution().maximizeSquareHoleArea(2,1,[2,3],[2]))