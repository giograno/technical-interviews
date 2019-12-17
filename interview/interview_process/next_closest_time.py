import unittest


class Solution:
    def nextClosestTime(self, time: str) -> str:
        hours = int(time[:2])
        minutes = int(time[3:5])
        allowed = set([int(time[0]), int(time[1]), int(time[3]), int(time[4])])
        while True:
            minutes += 1
            if minutes >= 60:  # reset minutes and increase hours
                minutes = 0
                hours += 1
                if hours > 23:  # reset time if midnight
                    hours = 0
            if self.matches("{0:02d}".format(hours) + "{0:02d}".format(minutes), allowed):
                return "{0:02d}:{1:02d}".format(hours, minutes)

    def matches(self, time: str, allowed: set()) -> bool:
        for i in [int(d) for d in time]:
            if i not in allowed: return False
        return True


class TestSolution(unittest.TestCase):

    def test_solution(self):
        sol = Solution()
        ans = sol.nextClosestTime("23:59")
        self.assertEqual(ans, "22:22")


if __name__ == '__main__':
    unittest.main()