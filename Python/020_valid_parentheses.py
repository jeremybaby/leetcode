class Solution:
    def isValid(self, s):

        stack = []
        lookup = {'(': ')', '[': ']', '{': '}'}

        for parenthese in s:
            # push left parenthese
            if parenthese in lookup:
                stack.append(parenthese)
            # pop right parenthese and compare
            elif len(stack) == 0 or parenthese != lookup[stack.pop()]:
                # Attention:  "]"
                return False
            # Attention : "["
        return len(stack) == 0
