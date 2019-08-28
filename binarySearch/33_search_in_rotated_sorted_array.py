class Solution:
    def search(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif  nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            print("mid: ", mid, "low: ", low, "high: ", high)
        return -1
            
s = Solution()
print(s.search([3, 1], 1))
