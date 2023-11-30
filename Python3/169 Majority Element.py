# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # create a dictionary of nums and count the occurences
        # return key with max value in dictionary
        count = {}
        length = len(nums)

        for i in range(length):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        value = 0
        for i in count:
            if value == 0 or value < count[i]:
                value = count[i]
                ans = i

        return ans
        