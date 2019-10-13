class Solution:
    """把当前目录压入栈中,遇到..弹出栈顶,最后返回栈中元素"""
    def simplifyPath(self, path):

        stack = []
        path = path.split("/")

        for item in path:
            if item == "..":
                if stack:
                    stack.pop()

            elif item and item != '.':
                stack.append(item)
            print('item: ', item, 'stack: ', stack)

        return "/" + "/".join(stack)