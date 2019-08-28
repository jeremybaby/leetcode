#include <stdio.h>

int searchInsert(int *nums, int numsSize, int target){
	int low = 0;
	int high = numsSize; // [0, numsSize)
	while (low < high) {
		int mid = low + (high - low) / 2;
		if (target < nums[mid])
			high = mid;
		else if(target > nums[mid])
			low = mid + 1;
		else
			return mid;
	}
	return low;
}

/*
[1,3,5,6]
2
*/

int main() {
	int arr[4] = {1, 3, 5, 6};
	int len = 4;
	printf("Result is %d\n", searchInsert(arr, len, 2));
	return 0;
}