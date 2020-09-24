class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """返回字符串t中比字符串s中多出的那个小写字母
        思路：
            由于全是小写字母，且只有一个字母的区别。
            可将s和t的字母全都转换为ascii码后相加，再作差，
            得到的数字就是多出那个字母的ascii码。
        """
        sum_s = sum([ord(c) for c in s])
        sum_t = sum([ord(c) for c in t])
        return chr(sum_t - sum_s)