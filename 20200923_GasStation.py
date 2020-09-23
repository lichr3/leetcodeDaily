class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        """
        思考：
        1. 由于是一个circle route，算法应该需要遍历完整个序列
        2. 每一个gas[i] - cost[i] > 0 的 i 都可能是正确答案，如何从中甄别?
        算法：
        1. 从i=0开始寻找第一个gas[i]-cost[i]>=0的i，并记录 idx = i, total = gas[i] - cost[i]
        2. 令 total = total + gas[i] - cost[i], 当total<0时令 idx=-1，total=-1
        3. 开始寻找下一个gas[i]-cost[i]>=0的i，记录idx=i, total = gas[i] - cost[i]
        4. 重复执行步骤2和3，最后得到的idx就是结果
        """
        if sum(gas) < sum(cost):
            return -1
        total = -1
        idx = -1
        for i in range(len(gas)):
            if total == -1 and (gas[i] - cost[i] >= 0):
                total = gas[i] - cost[i]
                idx = i
            elif total != -1:
                total += gas[i] - cost[i]
                if total < 0:
                    total = -1
                    idx = -1
        return idx


test = Solution()
gas = eval(input("input gas list: "))
cost = eval(input("input cost list: "))
print("result is ", test.canCompleteCircuit(gas, cost))
