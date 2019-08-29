class Solution:
    # Solution 1: Prepare with the front
    def romanToInt(self, s):

        num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(s)):
            if i > 0 and num_map[s[i]] > num_map[s[i-1]]:
                result += num_map[s[i]] - 2 * num_map[s[i-1]]
            else:
                result += num_map[s[i]]
        return result

    # Solution 2: Prepare with the next, it's better
    def romanToInt2(self, s):

        num_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and num_map[s[i]] < num_map[s[i + 1]]:
                result -= num_map[s[i]]
            else:
                result += num_map[s[i]]
        return result


