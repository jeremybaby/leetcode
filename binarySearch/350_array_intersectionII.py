class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
        	return self.intersect(nums2, nums1)

        lookup = collections.defaultdict(int) #初始化为0
        for i in nums1:
        	lookup[i] += 1

        result = []
        for i in nums2:
        	if lookup[i] > 0:
        		result += i,
        		lookup[i] -= 1

        return result

        