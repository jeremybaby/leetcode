#include <stdio.h>
/* version 1.0 */
int mySqrtBS(int x){
	if (x <= 1) return x;
	long long low = 0;
	long long high =(long long)x + 1; 

	while (low < high) {
		long long mid = low + (high - low) / 2;
		if (x < mid * mid) // 找到一个min的m使得 m*m > x
			high = mid;
		else if (x > mid * mid)
			low = mid + 1;
		else
			return mid;
	}
	return low - 1;
}

// To Promote:
// 1. high最小可以为 x/2+1
// 	对于一个非负数n，它的平方根不会小于大于（n/2+1） ？？？
//  A = sqrt(x) VS. B = (n/2) + 1
//  B^2 - A^2 = x^2/4 + 1 恒 > 0，证毕
// 2. long long 是否想办法可以去掉？

/* version 1.1 */
int mySqrtBS(int x){
	if (x <= 1) return x;
	int low = 1;
	int high = x / 2 + 1; // [1, x/2+1)

	while (low < high) {
		int mid = low + (high - low) / 2;
		if (mid > x / mid) // 不要写 x < mid * mid
			high = mid;
		else
			low = mid + 1;
	}
	return low - 1;
}

/* Solution2: Newton迭代法 */
#include <stdlib.h>
int mySqrt(int x){
	if (x <= 1) return x; // 0或1返回
	double cur = x; // 从x处开始迭代
	double EPS = 1e-6;
	while (fabs(pow(cur, 2) - x) > EPS) { // 注意循环是>
		cur = (cur + x / cur) / 2;
		printf("cur = %f\n", cur);
	}
	return cur;
}

int main() {
	int x = 2;
	printf("Result is %d\n", mySqrt(x));
}