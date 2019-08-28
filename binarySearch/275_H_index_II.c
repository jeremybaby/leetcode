
int hIndex(int* citations, int citationsSize){
	int low = 0;
	int high = citationsSize;

	while (low < high) {
		int mid = low + (high - low) / 2;
		if (citations[mid] < citationsSize - mid)
			low = mid + 1;
		else
			high = mid;
	}  
	// return citations[low]; // 会报错：传入空数组时此时会出错
	return citationsSize - low;
}

int hIndex(int* citations, int citationsSize){
	int low = 0;
	int high = citationsSize;

	while (low < high) {
		int mid = low + (high - low) / 2;
		if (citations[mid] > citationsSize - mid) // ❌，改为>=
			high = mid;
		else
			low = mid + 1;

	}  
	return citationsSize - low;
}