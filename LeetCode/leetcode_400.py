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
            d = 9 * 10 ** i  # 从9，90,900递推看在哪一层次的数上
            if n <= (i + 1) * d: break
            n = n - (i + 1) * d
        n -= 1
        return int(str(10 ** i + n / (i + 1))[n % (i + 1)])


sl = Solution()
print sl.findNthDigit(1000000000)


"""
分析可以得出一位有９个数字，二位数有90个数字，三位数有900个数，依次类推．
因此可以每次增加一位数字，看n是否还在这个范围内．
例如给定n = 150，首先一位有９个数字，所以位数可以＋１，这样n-9 = 141. 
然后２位的数字有２＊９０= 180，大于１４１，所以目标数字肯定是２位的．
然后求具体落在哪个数字．可以用10+(141-1)/2 = 80求出．
再求具体落在哪一位上，可以用(141-1)%2＝０求出为第０位，即８．如此即可．
"""