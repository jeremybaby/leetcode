class Solution:
    def lengthOfLastWord(self, s):

        local_count = 0
        # For circumstance:
        #   "Hello " to keep the last value
        result = 0

        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0
            else:
                local_count += 1
                result = local_count

        return result
