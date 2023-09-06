# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prefix = 1
        for i in nums:
            ans.append(prefix)
            prefix *= i
        
        postfix = 1
        for i in reversed(range(len(nums))):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans