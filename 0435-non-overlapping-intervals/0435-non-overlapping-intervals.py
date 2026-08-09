class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x: x[1])

        removals = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):

            # overlap
            if intervals[i][0] < end:
                removals += 1

            # no overlap -> keep it
            else:
                end = intervals[i][1]

        return removals