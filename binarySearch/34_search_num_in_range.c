#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
	if (returnSize)
		*returnSize = 2;
    int low = 0, i;
    int high = numsSize;
    int *result = (int *)malloc(2 * sizeof(int));
    result[0] = -1;
    result[1] = -1;

    while (low < high) {
    	int mid = low + (high - low) / 2;
    	if (target > nums[mid])
    		low = mid + 1;
    	else if (target < nums[mid])
    		high = mid;
    	else {
    		result[0] = mid;
    		while (nums[mid] == target)
    			++mid;
    		result[1] = mid - 1;
    		return result;
     	}
    }
    return result;
}

int main() {
	int nums[10] = {5, 7, 7, 8, 8, 10};
	int len = 6;
	int target = 7;
	int size;
	int *res = searchRange(nums, len, target, &size);
	printf("Result of [");
	for (int i = 0; i < 2; i++)
		printf("%d,", res[i]);
	printf("]\n");
	return 0;
}

