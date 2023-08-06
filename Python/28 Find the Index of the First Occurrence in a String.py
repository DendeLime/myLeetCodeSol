# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)
    
# KMP (Knuth-Morris-Pratt) algorithim

# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """

#         lenHay = len(haystack)
#         lenNeed = len(needle)

#         lps = [0] * lenNeed # Longest Prefix Suffix
#         index = 0
#         for i in range(1, lenNeed):
#             while (index > 0 and needle[i] != needle[index]):
#                 index = lps[index - 1]
#             if needle[index] == needle[i]:
#                 index += 1
#                 lps[i] = index
        
#         n = 0
#         for h in range(lenHay):
#             while (n > 0 and needle[n] != haystack [h]):
#                 n = lps[n - 1]
#             if needle[n] == haystack[h]:
#                 n += 1
#             if n == len(needle):
#                 return h - n + 1
#         return -1
