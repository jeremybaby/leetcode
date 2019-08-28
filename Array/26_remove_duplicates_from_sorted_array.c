
int removeDuplicates(int *nums,int numsSize) {
	if (numsSize == 0) return 0;
	int count = 1;
	for (int i = 1; i < numsSize; i++) {
		if (nums[i] != nums[i-1]) {
			nums[count++] = nums[i];
		}
	}
	return count;
}

int main() {
	int arr[20] = {0,0,1,1,1,2,2,3,3,4};
	int arr2[3] = {1, 1, 2};
	int res[] = {};
	printf("Result: %d\n", removeDuplicates(arr2, 3));
	return 0;
}

