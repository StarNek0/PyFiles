# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/17 17:42'

# List = []
# List = raw_input()
# print List

List = [2, 7, 11, 15]
target = 9


class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

so = Solution()
print so.twoSum(List, target)