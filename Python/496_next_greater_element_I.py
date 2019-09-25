class Solution:
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