class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        #this variable will store the maximum side length of a square found so far
        s = 0
        #shorter references for readability
        bl = bottomLeft
        tr = topRight
        #number of rectangles
        n = len(bl)
        #compare every pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                #find overlapping region on the x-axis
                min_x = max(bl[i][0], bl[j][0])   # left boundary of overlap
                max_x = min(tr[i][0], tr[j][0])   # right boundary of overlap
                # find overlapping region on the y-axis
                min_y = max(bl[i][1], bl[j][1])   # bottom boundary of overlap
                max_y = min(tr[i][1], tr[j][1])   # top boundary of overlap
                # check if there is a valid overlapping rectangle
                if min_x < max_x and min_y < max_y:
                    # the largest square that can fit inside the overlap
                    # is limited by the smaller of width and height
                    length = min(max_x - min_x, max_y - min_y)
                    # Update the maximum square side length found
                    s = max(s, length)
        # Return the area of the largest square
        return s * s
# Test cases
print(Solution().largestSquareArea([[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]]))
print(Solution().largestSquareArea([[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]]))
