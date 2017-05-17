# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/17 17:34'
'''仍然是回文数'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = str(x)
        if x1 == x1[::-1]:
            return True
        else:
            return False
