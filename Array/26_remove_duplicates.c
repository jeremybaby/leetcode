#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
	int i, len;

	if (numsSize < 1) {
		return 0;
	}

	len = 1;
	for (i = 1; i < numsSize; i++) {
		if (nums[i] == nums[i-1])
			continue; 
		nums[len++] = nums[i];
	}
	return len;
}

int main() {
	int i;
	// int nums[3] = {1, 1, 2};
	int nums[10] = {0,0,1,1,1,2,2,3,3,4};
	int len = removeDuplicates(nums, 10);
	printf("Len: %d\n", len);
	for (i = 0; i < len; i++) {
		printf("%d ", nums[i]);
	}
    return 0;
}

