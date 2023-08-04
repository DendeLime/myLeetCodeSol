# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        revStr = x[::-1] # Reverse String
                         # https://www.w3schools.com/python/python_howto_reverse_string.asp
        
        if x == revStr:
            return True
        else:
            return False

        


# initial Radix sort solution

# import math
# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
#         if x == 0:
#             return True

#         digit_num = int(math.log10(x)) + 1
#         digitList = []
#         for i in range(digit_num):
#             num = x//10**i % 10
#             digitList.append(num)
#         for j in range(int(digit_num/2)):
#             if digitList[j] != digitList[digit_num-1-j]:
#                 return False
#         return True
