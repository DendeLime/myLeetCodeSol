class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = nums[len(nums)/2]
        return ans