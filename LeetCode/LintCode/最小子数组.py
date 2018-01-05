# coding:utf8
# __auth__ = zsdzzydos@gmail.com
# __date__ = 2017/9/18 10:17
# __sys__ = Win7 SP1
# __python_version__ == 2.7.13
"""
最小子数组 minimum-subarray
@desc: 给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。
@simple_input: [1, -1, -2, 1]
@simple_output: -3
"""


class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        n = len(nums)
        minSum = sum(nums)
        curSum = 0
        for i in range(n):
            # 从i开始求和，如果当前和小于于minSum,则赋值给minSum
            curSum += nums[i]
            if curSum < minSum:
                minSum = curSum
            # 前面的和如果已经大于0了，那么加上下一个元素值，肯定是大于下一个元素值
            # 所以如果前面加起来的值大于0了，则舍弃前面的和，从下一位开始继续求和
            if curSum > 0:
                curSum = 0
        return minSum

if __name__ == "__main__":
    solution = Solution()
    print solution.minSubArray([1, -1, -2, 1])


# nums = [1, -1, -2, 1]
# nums_min = 2147483647
# if len(nums) > 1:
#     for i in range(1, len(nums)):
#         num = nums[i] + nums[i - 1]
#         if num < nums_min:
#             nums_min = num
# else:
#     print nums[0]
# print nums_min
