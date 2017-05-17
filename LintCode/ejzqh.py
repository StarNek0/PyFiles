# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/17 18:20'
'''二进制求和'''
# eval('0b111')把二进制字符串化为十进制
# 或者是以下这种
# print int('111', base=2)


class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        a = int(str(a), base=2)
        b = int(str(b), base=2)
        return bin(a+b).replace('0b', '')  # 结果要求没有0b。。。所以用replace替换掉了

if __name__ == '__main__':
    so = Solution()
    print so.addBinary(11, 1)