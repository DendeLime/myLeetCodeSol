# https://leetcode.com/problems/group-anagrams/description/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}

        for i in strs:
            sort = "".join(sorted(i))

            if sort not in anagrams:
                anagrams[sort] = []
            anagrams[sort].append(i)
            
        return list(anagrams.values())