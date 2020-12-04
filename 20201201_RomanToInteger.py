class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0:
            return 0

        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        if len(s) == 1:
            return romanDict[s]

        result = 0
        tmp = 1

        for c in s[::-1]:
            if tmp <= romanDict[c]:
                result += romanDict[c]
            else:
                result -= romanDict[c]
            tmp = romanDict[c]
        return result


test = Solution()
print(test.romanToInt("IX"))

