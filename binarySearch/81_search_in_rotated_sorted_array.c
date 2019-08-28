
bool search(int* nums, int numsSize, int target){
    if (numsSize == 0) return false;
    int low = 0;
    int high = numsSize - 1;
    while (low <= high) {
    	int mid = low + (high - low) / 2;
    	if (nums[mid] == target)
    		return true;
    	else if (nums[mid] > nums[low]) {
    		if (target >= nums[low] && target < nums[mid])
    			high = mid - 1;
    		else
    			low = mid + 1;
    	} else if (nums[mid] < nums[low]){
    		if (target > nums[mid] && target <= nums[high])
    			low = mid + 1;
    		else
    			high = mid - 1;
    	} else
    		low++;
    }
    return false;
}
