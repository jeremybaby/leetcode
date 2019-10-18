class Solution1_1:
    """先排序，比较相邻元素大小"""
    def minimumAbsDifference(self, arr):

        ans = []
        min_num = float('inf')

        arr.sort()

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]

            if diff < min_num:
                min_num = diff
                ans = [[arr[i], arr[i + 1]]]
            elif diff == min_num:
                ans.append([arr[i], arr[i + 1]])

        return ans


import collections

class Solution1_2:
    def minimumAbsDifference(self, arr):
        res = collections.defaultdict(list)

        arr.sort()

        for i in range(len(arr) - 1):
            res[arr[i + 1] - arr[i]].append([arr[i], arr[i + 1]])

        return res[min(res.keys())]


class Solution2:
    """
      最值问题，既然要求最小绝对值差，我们就从最小的开始逐个试.
      - Step1：先将数组转成set，用于哈希查找
      - Step2: 对于数组中的每个元素ele, 从dist = 1开始
            -  看ele + dist在不在数组中，如果在，我们返回所有的这样的元素
            -  此时的dist即为最小距离
      - Step3：对结果数组进行排序，返回
    """
    def minimumAbsDifference(self, arr):
        arr_set = set(arr)

        dist, result = 0, []

        while not result:
            # dist从1开始累加
            # 如果ele + dist在数组中，dist即为最短距离
            dist += 1
            result = [ele for ele in arr if ele + dist in arr_set]

        return [[ele, ele + dist] for ele in sorted(result)]