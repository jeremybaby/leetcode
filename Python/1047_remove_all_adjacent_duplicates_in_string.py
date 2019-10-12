class Solution1_1:
    """stack版"""
    def removeDuplicates(self, S):

        stack = []

        for s in S:
            if stack and s == stack[-1]:
                stack.pop()
            else:
                stack.append(s)

        return ''.join(stack)

class Solution1_2:
    """字符串版"""
    def removeDuplicates(self, S):
        ans = ''

        for s in S:
            if ans and s == ans[-1]:
                ans = ans[:-1]
            else:
                ans += s

        return ans


from string import ascii_lowercase

class Solution:
    """"""
    def removeDuplicates(self, S):

        duplicates = {2 * ch for ch in ascii_lowercase}

        prev_len = -1

        while prev_len != len(S):

            prev_len = len(S)

            for ch in duplicates:
                S = S.replace(ch, '')

        return S