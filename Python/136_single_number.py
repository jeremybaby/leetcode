class Solution1:
    """ 建立一个不重复的list
        遍历list
        - 不在list中，append进去
        - 在list中，remove
        时间复杂度：O(n^2)：遍历O(n)，查找O(n)
        空间复杂度：O(n)
        目的：熟悉list的一些操作
    """
    def singleNumber(self, nums):
        no_repeat_list = []

        for i in nums:
            if i not in no_repeat_list:
                no_repeat_list.append(i)
            else:
                no_repeat_list.remove(i)
                
        return no_repeat_list.pop()


class Solution2:
    """ 哈希表：
    遍历数组中的每个数字，
    - 若当前数字已经在HashSet中，则将HashSet中的该数字移除，
    - 否则就加入HashSet。
    这相当于两两抵消了，最终出现两次的数字都被去除了，
    唯一剩下的那个就是单独数字了
    """
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


class Solution3:
    """ 位运算
    如果我们对 0 和二进制位做 XOR 运算，得到的仍然是这个二进制位
        a ⊕ 0 = a
    如果我们对相同的二进制位做 XOR 运算，返回的结果是 0
        a ⊕ a = 0
    XOR 满足交换律和结合律
        a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b
    """

    def singleNumber(self, nums):
        ans = 0

        for num in nums:
            ans = ans ^ num

        return ans

class Solution4:
    """ Math:
        2∗(a+b+c)−(a+a+b+b+c)=c
    """
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)