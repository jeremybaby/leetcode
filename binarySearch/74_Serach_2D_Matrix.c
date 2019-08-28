#include <stdio.h>
#include <stdbool.h> /* C99 only */

/* Solution1: 二维 -—> 一维 的坐标mapping */
/* 算法复杂度 log(mn) = logm + logn */
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target){
	if (matrixSize == 0 || *matrixColSize == 0) return false;
	int low = 0;
	int high = matrixSize * (*matrixColSize) - 1;
	while (low <= high) {
		int mid = low + (high - low) / 2;
		int row = mid / *matrixColSize;
		int col = mid % *matrixColSize;
		if (target == matrix[row][col])
			return true;
		else if (target > matrix[row][col])
			low = mid + 1;
		else
			high = mid - 1;
	}
	return false;
}

/* Solution2： 先对行二分，再对列二分 */
/* 时间复杂度：O(logm+logn)=O(log(mn)) */
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
	if (matrixSize == 0 || *matrixColSize == 0) return false;
	int startRow = 0, endRow = matrixSize - 1;
	int startCol = 0, endCol = *matrixColSize - 1;
	int midRow, midCol;
	while (startRow <= endRow) {
		midRow = startRow + (endRow - startRow) / 2;
        if (matrix[midRow][endCol] == target)
            return true;
		else if (matrix[midRow][endCol] < target)
            startRow = midRow + 1;			
		else {
            if (target < matrix[midRow][startCol])
                endRow = midRow - 1;
            else
                break;
        }
	}
	while (startCol <= endCol) {
		midCol = startCol + (endCol - startCol) / 2;
		if (matrix[midRow][midCol] < target)
			startCol = midCol + 1;
		else if (matrix[midRow][midCol] > target) 
			endCol = midCol - 1;
		else 
			return true;
	}
	return false;
}

/* Solution2 Promote */
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
	if (matrixSize == 0 || *matrixColSize == 0) return false;
	int startRow = 0, endRow = matrixSize - 1;
	int startCol = 0, endCol = *matrixColSize - 1;
	int midRow, midCol;
	while (startRow <= endRow) {
		midRow = startRow + (endRow - startRow) / 2;
        if (matrix[midRow][endCol] == target)
            return true;
		else if (matrix[midRow][endCol] < target)
            startRow++;	
		else 
			endRow--;
	}
	while (startCol <= endCol) {
		midCol = startCol + (endCol - startCol) / 2;
		if (matrix[midRow][midCol] < target)
			startCol = midCol + 1;
		else if (matrix[midRow][midCol] > target) 
			endCol = midCol - 1;
		else 
			return true;
	}
	return false;
}

int main() {
	int a[3][4] = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 50}};
		for (int i = 0; i < 3; i++)
		for (int j = 0; j < 4; j++)
			printf("%d ", a[i][j]);
	int *b;
	b = &a[0][0];
	int target = 1;
	int colSize = 4;
	bool res = searchMatrix2(&b, 3, &colSize, target);
	 printf("%d\n", (int)res);
	return 0;
}




