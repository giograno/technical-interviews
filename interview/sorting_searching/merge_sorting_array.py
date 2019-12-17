import unittest


class Solution:
    """
    First naive solution would be to merge the two arrays and then sort
    The complexity would be O((n+m)log(n+m))

    The second approach would be to copy the the array to sort and use two pointers from the beginning of the lists
    The time complexity is O(n+m) but the space complexity if O(m)

    Using pointers from the back, we can reduce space complexity to O(1)
    """
    def merge(self, nums1: [], m: int, nums2: [], n: int):
        insert = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[insert] = nums1[p1]
                p1 += -1
                insert += -1
            else:
                nums1[insert] = nums2[p2]
                p2 += -1
                insert += -1
        if p2 < 0:
            return
        nums1[:p2 + 1] = nums2[:p2 + 1]

