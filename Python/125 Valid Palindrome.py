# https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        strArr = []
        validChar = ''.join(i for i in s if i.isalnum()).lower()

        for i in range(len(validChar)/2):
            if validChar[i] != validChar[len(validChar) - i - 1]:
                return False
        return True