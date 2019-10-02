class Solution:
    """
        输入: [1,2,1]
        输出: [2,-1,2]
      - 单调栈: 从左至右，存储数组
      - 循环数组：通过余数，将数组的长度扩大两倍
    """
    def nextGreaterElements(self, nums):

        stack = []
        length = len(nums)
        res = [-1] * length

        for i in range(length * 2):
            num = nums[i % length]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            # 注意，小于的时候才append
            if i < length:
                stack.append(i)
        return res
    """
            [1, 2, 1, 1, 2, 1]
        num =    1   2     1      1       2       1
        res =   [ ] [2,,] [2,,]  [2,,]   [2,,2]   [2,,2]
        stack = [0] [1]   [1, 2] [1, 2]  [1]      [1]
    """