from operator import itemgetter


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort by each start -> each end
        sorted_intervals = sorted(intervals, key=itemgetter(0, 1))  # O(n*n)

        # find overlapping
        current_end = -5 * 10**4
        overlapped = 0
        for interval in sorted_intervals:  # O(n)
            if interval[0] < current_end:
                print("overlapped!")
                if interval[1] < current_end:
                    current_end = interval[1]
                overlapped += 1
            else:
                current_end = interval[1]

        return overlapped

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort by each start
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])  # O(n)

        # find overlapping
        current_end = -5 * 10**4
        overlapped = 0
        for interval in sorted_intervals:  # O(n)
            if interval[0] < current_end:
                if interval[1] < current_end:
                    current_end = interval[1]
                overlapped += 1
            else:
                current_end = interval[1]

        return overlapped


# test
if __name__ == "__main__":
    s = Solution()
    s.eraseOverlapIntervals([[1, 3], [2, 3], [3, 4], [1, 2]])
    s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])
    s.eraseOverlapIntervals([[1, 3], [2, 4], [3, 6], [4, 5]])
    s.eraseOverlapIntervals([[1, 5], [0, 3], [3, 6], [4, 5]])
    s.eraseOverlapIntervals([[10, 11], [1, 5], [2, 3], [3, 4]])
