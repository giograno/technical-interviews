class Solution:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    """
    def findMin(self, nums: [int]) -> int:
        """
        Complexity:
            O(n) time
            O(1) space
        """
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return nums[i+1]
        return nums[0]


    def findMinBinarySearch(self, nums: [int]) -> int:
        """
        Binary search.
        Look for the inflection point:
            All the elements to the left of inflection point > first element of the array.
                nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
            All the elements to the right of inflection point < first element of the array.
                nums[mid - 1] > nums[mid] Hence, mid is the smallest.
        """
        if len(nums) == 1:
            return nums[0]

        start = 0
        end = len(nums) - 1

        # there is no rotation
        if nums[end] > nums[0]:
            return nums[0]

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]  # we found an inflation point
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                start = mid + 1
            else:
                end = mid - 1
