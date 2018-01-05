# coding:utf8
"""
-------------------------------------------------
    File:   leetcode_400.py
    Auth:   zsdostar
    Date:   2017/11/20 21:45
    Sys:    Windows 10
-------------------------------------------------
    Desc:   400. Nth Digit
            https://leetcode.com/problems/
            nth-digit/description/
            Find the nth digit of the infinite-
            integer sequence-
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
-------------------------------------------------
"""
__author__ = 'zsdostar'


# 极慢的方法，炸内存，仅仅用作验证
# class Solution(object):
#     def findNthDigit(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         s = ''.join([str(i) for i in range(1,n+1)])
#         return int(s[i-1])

# 也很慢，没跑过，炸内存
# class Solution(object):
#     def findNthDigit(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         length = 0
#         res = 0
#         for i in range(1, n + 1):
#
#             length += len(str(i))
#             if length >= n:
#                 res = int(str(i)[len(str(i)) - (length - n) - 1])
#                 break
#         return res


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(9):
            d = 9 * 10 ** i
            if n <= d * (i + 1):
                break
            n -= d * (i + 1)
        n -= 1
        return int(str(10 ** i + n / (i + 1))[n % (i + 1)])


if __name__ == '__main__':
    res = Solution()
    print res.findNthDigit(110)
