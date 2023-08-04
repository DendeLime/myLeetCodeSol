# https://leetcode.com/problems/plus-one/description/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numStr = ""
        for i in digits:
            numStr += str(i)
        numInt = int(numStr) + 1
        ans = [int(j) for j in str(numInt)]
        return ans