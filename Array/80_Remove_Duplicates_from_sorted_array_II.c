#include <stdio.h>



int removeDuplicates(int* nums, int numsSize){
	if (numsSize == 0) return 0;
	int count = 0;
	int len = 1;
	for (int i = 1; i < numsSize; i++) {
		if (nums[i] != nums[i-1]) {
			count = 0;
			nums[len++] = nums[i]; 
		} else {
			++count;
			if (count < 2) {
				nums[len++] = nums[i]; 
			}
		}
	}
	return len;
}

//  [1,1,1,2,2,3]

int main() {
	int arr[] = {1,1,1,2,2,3};
	removeDuplicates(arr, 6);
	for (int i = 0; i < 6; i++)
		printf("%d ", arr[i]);
	return 0;
}