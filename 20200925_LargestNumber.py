# 题目：https://leetcode.com/problems/largest-number/
# 答案：https://leetcode.com/problems/largest-number/solution/
# 相关证明：https://leetcode.com/problems/largest-number/discuss/291988/A-Proof-of-the-Concatenation-Comparator's-Transtivity

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # 如果nums全为0则返回0
        return '0' if largest_num[0] == '0' else largest_num


test = Solution()
print(test.largestNumber(eval(input("Input: "))))

