# https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        found = 0
        if len(s) > len(t):
            return False
        for i in range(len(t)):
            if found < len(s) and s[found] == t[i]:
                found += 1
        if found != len(s):
            return False
        return True