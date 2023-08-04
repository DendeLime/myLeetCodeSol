# https://leetcode.com/problems/longest-common-prefix/submissions/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        strs.sort()
        word1 = strs[0]
        word2 = strs[len(strs)-1]
        smaller = min(word1, word2)

        for j in range(len(smaller)):
            if word1[j] == word2[j]:
                prefix = prefix + word1[j]
            else:
                break

        for i in strs:
            if prefix != i[0:len(prefix)]:
                return ""
        return prefix