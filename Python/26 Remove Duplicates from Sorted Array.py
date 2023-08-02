# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# side note: This proplem is terrible in explanation and most methods of removing duplicates(python) arent excepted for some reason.
# As of time of posting 12k upvotes and 15.9k downvotes
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[count] = nums[i]
                count +=1
        return count