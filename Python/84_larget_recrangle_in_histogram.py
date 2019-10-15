import sys


class Solution:
    def largestRectangleArea(self, heights):

        stack = [-1]
        maxarea = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                maxarea = max(maxarea, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            temp = heights[stack.pop()] * (len(heights) - stack[-1] - 1)
            maxarea = max(maxarea, temp)

        return maxarea