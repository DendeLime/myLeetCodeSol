# https://leetcode.com/problems/rotate-array/ 

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        shift = k % len(nums)
        temp = nums[(length - shift):length] # slice end shift

        # add the rest of the numbers after the shift
        for i in range(len(nums) - shift):
            temp.append(nums[i])

        # copy order to nums array
        for i in range(length):
            nums[i] = temp[i]