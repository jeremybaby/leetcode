#include <stdio.h>

/* 方法一: 排序 O(nlgn)找第一个 */
/* 方法二: 遍历 O(n) */


int findMin(int* nums, int numsSize) {
	int low = 0;
	int high = numsSize - 1;
	while (low <= high) {
		int mid = low + (high - low) / 2;
		if (nums[mid] > nums[low]) { // sorted left
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}
}

/* Solution 2 */
#define min(x,y) ((x) < (y) ? (x) : (y))

int findMin(int* nums, int numsSize) {
    if (numsSize == 1) return nums[0];
	int low = 0;
	int high = numsSize - 1;
	if (numsSize == 2) return min(nums[low], nums[high]);
	if (nums[low] < nums[high])
		return nums[low];
	int mid = low + (high - low) / 2;
	return min(findMin(&nums[low], mid - low + 1), findMin(&nums[mid], high-mid+1));
}
