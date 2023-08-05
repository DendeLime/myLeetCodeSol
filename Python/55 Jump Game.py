# https://leetcode.com/problems/jump-game/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True

        pos = nums[0]

        for i in range(1, len(nums)):

            if i <= pos:
                pos = max(pos, i + nums[i])
            else:
                return False

        return True
