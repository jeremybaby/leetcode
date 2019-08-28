class Solution:
    def intersection(self, nums1, nums2):
    	#lookup越小越好
    	if len(nums1) > len(nums2):
    		return self.intersection(nums2, nums1)
    	
    	# lookup = set()
    	# for i in nums1:
    	# 	lookup.add(i)
    	lookup = set(nums1)

    	result = []
    	for i in nums2:
    		if i in lookup:
    			result += i,
    			lookup.discard(i)

    	return result
