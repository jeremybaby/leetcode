class Solution:
    # Solution1: Based on the 1st str, compare with the others.
    def longestCommonPrefix(self, strs):

        # []
        if not strs:
            return ""

        first_str = strs[0]

        for i in range(len(first_str)):
            for str in strs[1:]:
                if i >= len(str) or str[i] != first_str[i]:
                    return first_str[:i]

        # Contains only one str: [""] or ["a"] or ["abc"]
        return first_str

    # Solution2: Use the advantage of set(), put str[i] into one set.
    def longestCommonPrefix2(self, strs):

        result = ""
        i = 0

        while True:
            try:
                sets = set(str[i] for str in strs)
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except:
                break

        return result

