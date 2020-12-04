class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if len(timeSeries) == 0 or duration == 0:
            return 0
        total = 0
        beg, end = timeSeries[0], timeSeries[0] + duration
        for timepoint in timeSeries[1:]:
            if timepoint <= end:
                end = timepoint + duration
            else:
                total += end - beg
                beg = timepoint
                end = timepoint + duration
        total += end -beg
        return total

test = Solution()
timeSeries = eval(input("timeSeries: "))
duration = eval(input("duration:"))
print(test.findPoisonedDuration(timeSeries, duration))
