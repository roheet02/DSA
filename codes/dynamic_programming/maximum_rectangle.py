from typing import List
class Solution:
    # helper function to calculate largest rectangle area in a histogram
    def largestRectangleArea(self, heights):
        n = len(heights)
        # stack will store indices of bars
        # we keep it monotonic increasing
        stack = [-1]
        # prevSmaller[i] -> index of previous smaller bar than heights[i]
        # nextSmaller[i] -> index of next smaller bar than heights[i]
        prevSmaller = [0] * n
        nextSmaller = [0] * n
        # find previous smaller element for each bar
        for i in range(n):
            # pop until current bar is greater than stack top
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            prevSmaller[i] = stack[-1]
            stack.append(i)
        # reset stack for next smaller calculation
        stack = [-1]
        # find next smaller element for each bar
        for i in range(n - 1, -1, -1):
            # pop until current bar is greater than stack top
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # if no smaller element, use n as boundary
            nextSmaller[i] = n if stack[-1] == -1 else stack[-1]
            stack.append(i)
        # calculate max area using height and width
        maxArea = 0
        for i in range(n):
            height = heights[i]
            # width between previous and next smaller bar
            width = nextSmaller[i] - prevSmaller[i] - 1
            maxArea = max(maxArea, height * width)
        return maxArea
    # main function to find maximal rectangle of 1s in binary matrix
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # edge case: empty matrix
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        # histogram represents heights of consecutive 1s column-wise
        histogram = [0] * cols
        answer = 0
        # build histogram row by row
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    histogram[j] += 1
                else:
                    # reset height if current cell is 0
                    histogram[j] = 0
            # for each row, compute max rectangle using histogram
            answer = max(answer, self.largestRectangleArea(histogram))
        return answer
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

print(Solution().maximalRectangle(matrix))