# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1 += nums2
        nums1.sort()

        while 0 in nums1 and len(nums1) > (n+m):
            nums1.remove(0)

        return nums1