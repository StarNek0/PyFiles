# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/17 19:13'
'''买卖股票的最佳时机II'''
import sys


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        total = 0
        l, r = sys.maxint, sys.maxint
        for i in prices:
            if i <= r:
                total += r - l
                l, r = i, i
            elif i > r:
                r = i
        return total + r - l


if __name__ == '__main__':
    prices = [3, 2, 6, 5, 0, 3]  # [2, 1, 2, 0, 1]
    so = Solution()
    print so.maxProfit(prices)  # 2
