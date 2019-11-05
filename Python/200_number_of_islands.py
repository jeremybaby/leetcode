class UnionFind:
    def __init__(self, N):
        self._count = N
        self._id = [i for i in range(N)]
        self._sz = [1 for _ in range(N)]

    def root(self, p):
        while self._id[p] != p:
            p = self._id[p]
        return p

    def union(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)
        if rootP == rootQ: return

        if self._sz[rootP] < self._sz[rootQ]:
            self._id[rootP] = rootQ
            self._sz[rootQ] += self._sz[rootP]
        else:
            self._id[rootQ] = rootP
            self._sz[rootP] += self._sz[rootQ]
        self._count -= 1


class Solution3:
    """并查集"""
    def numIslands(self, grid):

        row = len(grid)

        if row == 0: return 0

        col = len(grid[0])

        def getIndex(x, y):
            return x * col + y

        # 不用像DFS和BFS4个方向都要尝试，只要看一看右面和下面
        directions = [(0, 1), (1, 0)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummyNode = row * col

        uf = UnionFind(dummyNode + 1)

        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(getIndex(i, j), dummyNode)
                if grid[i][j] == '1':
                    # 下方or右方如果是陆地，即 "1"，就要合并一下
                    # 下方or右方如果是水域的话，不用管
                    for direction in directions:
                        newX = i + direction[0]
                        newY = j + direction[1]
                        if newX < row and newY < col and grid[newX][newY] == '1':
                            uf.union(getIndex(i, j), getIndex(newX, newY))
        return uf._count - 1
