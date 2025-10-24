"""                                     Merge Intervals                 """


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        currentInterval = intervals[0]

        mergeIntervals = []

        for j in range(1, len(intervals)):
            nextInterval = intervals[j]

            if currentInterval[1] > nextInterval[0]:

                currentInterval[1] = max(currentInterval[1], nextInterval[1])

        return currentInterval

    print(currentInterval)
