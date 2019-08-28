#include <stdio.h>
#include <stdlib.h>

int Binary_Search(int *a, int n, int key) {
	int low, high, mid;
	low = 0;
	high = n - 1;
	while (low <= high) {
		mid = low + (high - low) / 2; 
		if (key < a[mid])
			high = mid - 1;
		else if (key > a[mid])
			low = mid + 1;
		else
			return mid;
	}
	return -1;
}

int myCompare(const void *elem1, const void *elem2) {
	int *p1, *p2;
	p1 = (int *) elem1; // *elem1 非法
	p2 = (int *) elem2; // *elem2 非法
	return *p1 - *p2;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
	if (returnSize)
		*returnSize = 2;
	int i, j;
	int *result = (int *)malloc(2 * sizeof(int));
	int *cpyNums = (int *)malloc(numsSize * sizeof(int));
	int pos = 0;
	// 这里保存数组是为了最终要返回原数组中的位序和二分查找用
	for (int k = 0; k < numsSize; k++) {
		cpyNums[k] = nums[k];
	}
	// nums已被快排成有序数组
	qsort(nums, numsSize, sizeof(int), myCompare);
	for (i = 0, j = numsSize - 1; i < j; ) {
		int sum = nums[i] + nums[j];
		if (sum > target) 
			--j;
		else if (sum < target) 
			++i;
		else 
			break;
	}

	// printf("i = %d, j = %d \n", i, j);
	if (i != j) { 
		int isset1 = 1, isset2 = 1;
		for (int k = 0; k < numsSize; k++) {
			if (isset1 && nums[i] == cpyNums[k]) {
				result[0] = k;
				isset1 = 0;
				continue;
			}
			if (isset2 && nums[j] == cpyNums[k]) {
				result[1] = k;
				isset2 = 0;
				continue;
			}
		}
		return result;
	}

    *returnSize = 0;
    free(result);
	return NULL;
}

int main() {
	// int returnSize, numsSize = 2, target = 6;
	// int nums[2] = {3, 3};
	// int *p;
	// p = twoSum(nums, numsSize, target, &returnSize);

	// int returnSize, numsSize = 4, target = 9;
	// int nums[4] = {2, 7, 11, 5};
	// int *p;
	// p = twoSum(nums, numsSize, target, &returnSize);

	// int returnSize, numsSize = 3, target = 6;
	// int nums[3] = {3, 2, 4};
	// int *p;
	// p = twoSum(nums, numsSize, target, &returnSize);
	for (int i = 0; i < 2; i++)
		printf("result[%d] = %d\n", i, p[i]);
	return 0;
}