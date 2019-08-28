// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

/* 写法2 */
int firstBadVersion(int n) {
	int low = 1;
	int high = n + 1; 

	while (low < high) {
		int mid = low + (high - low) / 2;
		if (isBadVersion(mid)) // 如果是坏的 从4开始
			high = mid;
		else
			low = mid + 1;
	}

	return low;
}

/* 写法1 */
int firstBadVersion(int n) {
	int low = 1;
	int high = n; 

	while (low <= high) {
		int mid = low + (high - low) / 2;
		if (isBadVersion(mid)) // 如果是坏的 从4开始
			high = mid - 1;
		else
			low = mid + 1;
	}

	return low;
}

int firstBadVersion(int n) {
	int low = 1;
	int high = n;

	while (low + 1 < high) {
		int mid = low + (high - low) / 2;
		if (isBadVersion(mid))
			high = mid;
		else
			low = mid;
	}
	if (isBadVersion(low))
		return low;
	// 无需else，只有两种结果
	return high;
}