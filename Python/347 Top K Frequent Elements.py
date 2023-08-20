# https://leetcode.com/problems/top-k-frequent-elements/description/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        return[num for num, freq in Counter(nums).most_common(k)]