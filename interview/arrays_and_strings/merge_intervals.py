class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # this solution assumes that the lists are ordered in ascending order by the first element
        intervals = sorted(intervals)

        l = len(intervals)
        i = 0  # first index

        ans = []
        while i < l:
            j = i + 1  # moving index

            start = intervals[i]

            while j < l:
                # check if can merge
                if start[1] >= intervals[j][0]:
                    # do the merge
                    start = [start[0], intervals[j][1]]
                    i += 1  # avoid to pass on a merged interval
                    j += 1
                elif intervals[j][0] <= start[1]:
                    i += 1  # avoid to pass on a merged interval
                    j += 1
                else:
                    break
            i += 1
            # add the interval to the answer
            ans.append(start)
        return ans

class SolutionLeetCode:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged