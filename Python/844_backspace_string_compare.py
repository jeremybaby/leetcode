class Solution1:
    """ stack O(n) space
        当然下面的两个list处理时也可以放入同一个函数，原理一样
    """
    def backspaceCompare(self, S, T):

        stack_s, stack_t = [], []

        for s in S:
            if s != '#':
                stack_s.append(s)
            elif stack_s:
                stack_s.pop();

        for t in T:
            if t != '#':
                stack_t.append(t)
            elif stack_t:
                stack_t.pop()

        return stack_s == stack_t


class Solution2:
    """ 倒序使用双指针, O(1) space
        对于S和T，我们才用双指针分别指向S与T的末尾，我们采用逆序处理，
        遇到#进行计数，‘#’代表需要抵消的字符个数
    """
    def backspaceCompare(self, S, T):

        i, j = len(S) - 1, len(T) - 1
        cnt_s, cnt_t = 0, 0

        while i >= 0 or j >= 0:

            # 对每个'#'进行计数，只要是'#'或刚才遇到'#'个数不为0
            while i >= 0 and (S[i] == '#' or cnt_s > 0):
                if S[i] == '#':
                    cnt_s += 1
                else:
                    cnt_s -= 1
                i -= 1

            while j >= 0 and (T[j] == '#' or cnt_t > 0):
                if T[j] == '#':
                    cnt_t += 1
                else:
                    cnt_t -= 1
                j -= 1

            if (i < 0) or (j < 0):
                return i == j

            if S[i] != T[j]:
                return False

            i -= 1
            j -= 1

        return i == j
