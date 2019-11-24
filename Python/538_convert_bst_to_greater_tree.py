class Solution(object):
    def convertBST(self, root):
        
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:

            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)

                if succ.left is None:
                    succ.left = node
                    node = node.right

                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root