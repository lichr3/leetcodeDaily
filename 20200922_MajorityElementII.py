class Solution:
    def majorityElement(self, nums: list) -> list:
        """返回数组nums中出现次数超过floor(n/3)次的数的列表

        发现规则如下：
        1.出现次数超过floor(n/3)的数至多有两个（n为数组长度）
        2.故设置两个变量(candidate1, candidate2)作为候选者存储出现次数最多的数，设置两个变量(count1, count2)作为计数器即可

        算法如下：
        1.如果当前元素等于其中一个候选者，则将相应的计数器自加一
        2.如果某一个计数器为0，且下一个元素不等于其余任何一个候选者，则将该元素作为候选者，计数器值设为1
        3.如果当前元素不等于任何一个候选者，所有计数器自减一
        4.通过以上三步选出两个候选者，再遍历一遍数组计算候选者出现次数是否超过floor(n/3)即可得出结果

        :param nums: 整数数组
        :return: 出现次数超过floor(n/3)次的数的列表
        """
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # 1st pass
        for n in nums:
            if n == candidate1:     # 如果当前元素等于其中一个候选者，则将相应的计数器自加一
                count1 += 1
            elif n == candidate2:
                count2 += 1
            else:   # 如果某一个计数器为0，且下一个元素不等于其余任何一个候选者，则将该元素作为候选者，计数器值设为1
                if count1 == 0:
                    candidate1 = n
                    count1 = 1
                elif count2 == 0:
                    candidate2 = n
                    count2 = 1
                else:               # 如果当前元素不等于任何一个候选者，所有计数器自减一
                    count1 -= 1
                    count2 -= 1

        # 2nd pass
        result = []
        count1, count2 = 0, 0
        for n in nums:
            if (n == candidate1):
                count1 += 1
            if (n == candidate2):
                count2 += 1

        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)

        return result



test = Solution()
array = eval(input("请输入一个数组："))
result = test.majorityElement(array)
print("该数组中超过floor(n/3)的数如下：")
print(result)
