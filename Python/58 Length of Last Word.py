# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strArr = s.split()
        
        return len(strArr[-1])
