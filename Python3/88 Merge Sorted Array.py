# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1) - 1
        n -= 1
        m -= 1
        
        while n >= 0:
                if nums1[m] > nums2[n] and m >= 0:
                    nums1[length] = nums1[m]
                    m -= 1
                else:
                    nums1[length] = nums2[n]
                    n -= 1
                length -= 1
            

            