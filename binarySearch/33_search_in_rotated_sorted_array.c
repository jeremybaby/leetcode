
int search(int* nums, int numsSize, int target){
	if (numsSize == 0)	return -1;

	int low = 0;
	int high = numsSize - 1;
	while (low <= high) {
		int mid = low + (high - low) / 2;
		if (nums[mid] == target)
			return mid;
		else if (nums[mid] < nums[low]) {// rotated array left
			if (target > nums[mid] && target <= nums[high])
				low = mid + 1;
			else
				high = mid - 1;
		} else { // sorted array left
			if (target >= nums[low] && target < nums[mid])
				high = mid - 1;
			else
				low = mid + 1;
		}
	}
	return -1;
}