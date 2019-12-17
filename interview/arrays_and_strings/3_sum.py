import unittest


class Solution:
    """
    Given an array `nums` of integers, are there elements a, b, c, in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum or 0.
    Example:
        Given array nums = [-1, 0, 1, 2, -1, -4]
        A solution set is :
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
    Complexity of the solution: O(n^2)
    """
    def three_sum(self, nums):
        end = len(nums)
        nums = sorted(nums)

        sols = []
        for index in range(end - 2):

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            i = index + 1
            j = end - 1

            curr = nums[index]
            while i < j:
                val = nums[i] + nums[j] + curr
                if val < 0:
                    i += 1
                elif val > 0:
                    j -= 1
                else:
                    to_add = [curr, nums[i], nums[j]]
                    sols.append([curr, nums[i], nums[j]])
                    # trick to speed up everything!
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
        return sols


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_solution(self):
        ans = self.solution.three_sum([82597, -9243, 62390, 83030, -97960, -26521, -61011, 83390, -38677, 12333, 75987, 46091, 83794, 19355, -71037, -6242, -28801, 324, 1202, -90885, -2989, -95597, -34333, 35528, 5680, 89093, -90606, 50360, -29393, -27012, 53313, 65213, 99818, -82405, -41661, -3333, -51952, 72135, -1523, 26377, 74685, 96992, 92263, 15929, 5467, -99555, -43348, -41689, -60383, -3990, 32165, 65265, -72973, -58372, 12741, -48568, -46596, 72419, -1859, 34153, 62937, 81310, -61823, -96770, -54944, 8845, -91184, 24208, -29078, 31495, 65258, 14198, 85395, 70506, -40908, 56740, -12228, -40072, 32429, 93001, 68445, -73927, 25731, -91859, -24150, 10093, -60271, -81683, -18126, 51055, 48189, -6468, 25057, 81194, -58628, 74042, 66158, -14452, -49851, -43667, 11092, 39189, -17025, -79173, 13606, 83172, 92647, -59741, 19343, -26644, -57607, 82908, -20655, 1637, 80060, 98994, 39331, -31274, -61523, 91225, -72953, 13211, -75116, -98421, -41571, -69074, 99587, 39345, 42151, -2460, 98236, 15690, -52507, -95803, -48935, -46492, -45606, -79254, -99851, 52533, 73486, 39948, -7240, 71815, -585, -96252, 90990, -93815, 93340, -71848, 58733, -14859, -83082, -75794, -82082, -24871, -1])
        self.assertTrue(len(ans) == 3)

    def test_solution2(self):
        ans = self.solution.three_sum([-2, 0, 1, 1, 2])
        self.assertTrue(ans[0] == [-2, 0, 2])
        self.assertTrue(ans[1] == [-2, 1, 1])

    def test_solution3(self):
        ans = self.solution.three_sum([-1, 0, 1, 2, -1, 4])
        self.assertTrue(ans[0] == [-1, -1, 2])
        self.assertTrue(ans[1] == [-1, 0, 1])


if __name__ == '__main__':
    unittest.main()
