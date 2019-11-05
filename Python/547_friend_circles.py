class WeightedQuickUnion(object):

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


class Solution:
    def findCircleNum(self, M):

        n = len(M)
        friend_circles = WeightedQuickUnion(n)
        for i in range(n):
            for j in range(n):
                if i != j and M[i][j] == 1:
                    friend_circles.union(i, j)

        return friend_circles._count
