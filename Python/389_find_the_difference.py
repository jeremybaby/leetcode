class Solution1_1:
    """ 把s和t的字符存储在两个dict中，并记录每个字母出现的次数：
        - t中的字符c不在s中，返回c
        - 如果字符c在两个dict中出现紫薯不同，返回c
    """
    def findTheDifference(self, s, t):

        from collections import defaultdict
        s_dict, t_dict = defaultdict(int), defaultdict(int)

        for i in s:
            s_dict[i] += 1

        for i in t:
            if i not in s_dict:
                return i
            t_dict[i] += 1

        for str in t:
            if s_dict[str] != t_dict[str]:
                return str


class Solution1_2:
    """同上"""
    def findTheDifference(self, s, t):

        for c in t:
            if c not in s:
                return c
            if s.count(c) != t.count(c):
                return c

class Solution1_3:
    """同上"""

    def findTheDifference(self, s, t):

        for i in t:
            if t.count(i)-s.count(i) == 1:
                return i

class Solution2:
    """
        t中所有字母的字节码 减去 s中所有的字节码
        再把结果转换为字符
    """
    def findTheDifference(self, s, t):
        return chr(sum([ord(c) for c in t]) - sum(ord(c) for c in s))


class Solution3:
    """ 位运算
        两个串中只有一个字符不同，而字符对应的是ASCII码
        把所有的串中的字符的ASCII码都异或一遍，结果就是最终的字符的ASCII码
    """
    def findTheDifference(self, s, t):

        ans = 0

        for c in s:
            ans ^= ord(c)

        for c in t:
            ans ^= ord(c)

        return chr(ans)


class Solution4:
    """转成列表后排序，逐个比较，都没有就是t的最后一个"""
    def findTheDifference(self, s, t):

        s_list, t_list = list(s), list(t)

        s_list.sort()
        t_list.sort()

        print(s_list)
        for i in range(len(s)):
            if s_list[i] != t_list[i]:
                return t_list[i]

        return t_list[-1]

class Solution5:
    """t转列表，列表中移除s中的每个字符"""
    def findTheDifference(self, s, t):
        t_list = list(t)

        for c in s:
            t_list.remove(c)

        return t_list[0]