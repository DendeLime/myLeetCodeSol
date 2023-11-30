# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # iterate and make a key map of string s and t
        #
        # check for isomorphic validation

        key1 = {}
        key2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            key1[s[i]] = t[i]
            key2[t[i]] = s[i]

        for i in range(len(key1)):
            if ((key1[s[i]] != t[i]) or (key2[t[i]] !=s[i])):
                return False

        return True

        