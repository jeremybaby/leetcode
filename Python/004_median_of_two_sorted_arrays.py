class Solution:
    """Solution1: 第一遍自己的写法"""
    """用一个新数组存储两个数组排好序的值，直接返回中间的位置"""
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                i += 1

        if i == len(nums1):
            nums += nums2[j:]
        if j == len(nums2):
            nums += nums1[i:]

        half = len(nums) // 2

        return nums[half] if len(nums) % 2 == 1 else (nums[half - 1] + nums[half]) / 2