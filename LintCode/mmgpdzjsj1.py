# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/17 19:01'
'''买卖股票的最佳时机I'''
import sys


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        total = 0
        low = sys.maxint
        for x in prices:
            if x - low > total:  # 利润中选最大的
                total = x - low
            if x < low:  # 日价格最小的
                low = x
        return total

if __name__ == '__main__':
    so = Solution()
    print so.maxProfit([3, 2, 3, 1, 2])
