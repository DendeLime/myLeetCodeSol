# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in _dict:
                return [_dict[ans], i]
            _dict[nums[i]] = i