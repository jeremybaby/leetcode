class Solution1:
    """Brute Force"""
    def nextGreaterElement(self, nums1, nums2):
        res = []

        for i in nums1:
            isExist = False
            pos = nums2.index(i)
            for j in nums2[pos:]:
                if j > i:
                    isExist = True
                    res.append(j)
                    break
            if not isExist:
                res.append(-1)

        return res

class Solution2:
    """单调栈: """
    def nextGreaterElement(self, nums1, nums2):

        dict, stack = {}, []
        # 建立一个从左往右单调递减的栈

        for n in nums2:
            # 只要有栈顶小于当前值就弹栈
            while stack and stack[-1] < n:
                dict[stack.pop()] = n
            stack.append(n)

        return [dict.get(i, -1) for i in nums1]
