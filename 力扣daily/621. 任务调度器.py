class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        count = {}  # 记录每一个任务出现的次数
        for c in tasks:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        longest = max(count.values())   # 记录单种任务出现最多的次数
        longestCnt = 0  # 记录有多少个任务出现次数最多，例如任务A和B都出现了4次，其余任务出现次数小于4
        for cnt in count.values():
            if cnt == longest:
                longestCnt += 1
        res1 = (longest - 1) * (n + 1) + longestCnt 
        res2 = len(tasks)
        return max(res1, res2)

test = Solution()
tasks = eval(input("输入任务列表："))
n = eval(input("输入n："))
print(test.leastInterval(tasks, n))