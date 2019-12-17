class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        l_num = len(nums)
        nums = sorted(nums)

        ans = []
        for fix_one in range(l_num - 3):
            for fix_two in range(fix_one + 1, l_num - 2):
                i, j = fix_two + 1, l_num - 1

                while i < j:
                    val = nums[fix_one] + nums[fix_two] + nums[i] + nums[j]
                    if val > target:
                        j -= 1
                    elif val < target:
                        i += 1
                    else:
                        l_ans = [nums[fix_one], nums[fix_two], nums[i], nums[j]]
                        if l_ans not in ans:
                            ans.append(
                                [nums[fix_one], nums[fix_two], nums[i], nums[j]]
                            )
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                        while i < j and nums[j] == nums[j - 1]:
                            j -= 1
                        j -= 1
                        i += 1
        return ans

import unittest


class TestSolution(unittest.TestCase):

    def test_solution(self):
        n = [-3, -2, -1, 0, 0, 1, 2, 3]
        t = 0
        sol = Solution()
        expected = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        self.assertTrue(sol.fourSum(n, t) == expected)


# Look https://www.geeksforgeeks.org/find-four-elements-that-sum-to-a-given-value-set-2/ for better solution