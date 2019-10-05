class Solution:
    def findRepeatedDnaSequences(self, s):

        ans, sets = set(), set()

        for i in range(len(s) - 9):

            substr = s[i:i + 10]

            if substr in sets:
                ans.add(substr)

            sets.add(substr)

        return list(ans)