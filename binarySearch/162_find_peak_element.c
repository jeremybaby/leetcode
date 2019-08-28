int findPeakElement(int* nums, int numsSize){
    int low = 0;
    int high = numsSize - 1; // 注意这里时size - 1，防止越界
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] < nums[mid + 1])
            low = mid + 1;
        else
            high = mid;
    }
    return low;
}