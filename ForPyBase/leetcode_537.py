# coding:utf8
"""
-------------------------------------------------
    File:   leetcode_537.py
    Auth:   zsdostar
    Date:   2017/11/19 22:28
    Sys:    Windows 10
-------------------------------------------------
    Desc:   https://leetcode.com/problems/
            complex-number-multiplication/
            description/
-------------------------------------------------
"""
__author__ = 'zsdostar'

import re


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        pattern = '(-)?(\d+)\+(-)?(\d+)i'
        xy1 = re.match(pattern, a).groups() # ('-', '86', '-', '72')

        xy2 = re.match(pattern, b).groups()

        if xy1[0] is not None:
            a1 = int('-' + xy1[1])
        else:
            a1 = int(xy1[1])

        if xy1[2] is not None:
            b1 = int('-' + xy1[3])
        else:
            b1 = int(xy1[3])

        if xy2[0] is not None:
            a2 = int('-' + xy2[1])
        else:
            a2 = int(xy2[1])

        if xy2[2] is not None:
            b2 = int('-' + xy2[3])
        else:
            b2 = int(xy2[3])

        return str(a1 * a2 - b1 * b2) + '+' + str(a1 * b2 + a2 * b1) + 'i'


if __name__ == "__main__":
    res = Solution()
    print res.complexNumberMultiply("78+-76i", "-86+72i")
