#include <stdio.h>

 int lower_bound(int *nums, int target, int len) {
 	int low = 0;
 	int high = len;
 	while (low < high) {
 		int mid = low + (high - low) / 2;
 		if (target <= nums[mid])
 			high = mid;
 		else
 			low = mid + 1;

 	}
 	return low;
 }

int upper_bound(int *nums, int target, int len) {
	int low = 0;
	int high = len;
	while (low < high) {
		int mid = low + (high - low) / 2;
		if (target < nums[mid])
			high = mid;
		else
			low = mid + 1;
		printf("mid = %d, low = %d, high = %d\n", mid, low, high);
	}
	return low;
}

 int main() {
 	int arr[20] = {1, 2, 2, 2, 4, 4, 5};
 	int target = 2;
 	int len = 7;
 	printf("Lower Bound: \n");
 	printf("The result if %d is : %d\n", 3, lower_bound(arr, 3, len)); // 4
 	printf("Upper Bound: \n");
 	printf("The result of %d is : %d\n", 5, upper_bound(arr, 5, len)); // 7
 }
