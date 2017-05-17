# coding:utf8
# __author__ = 'zsdostar'
# __date__ = '2017/5/17 16:06'
__doc__ = '''这是一个回文数的粗糙解法，用的是将整数变成字符串并翻转，然后判断。。。'''
# s = raw_input()
# s = s[::-1]
# print s


class Solution:
    # @param {int} num a positive number
    # @return {boolean} true if it's a palindrome or false
    def palindromeNumber(self, num):
        # Write your code here
        num = str(num)
        numr = num[::-1]
        if numr == num:
            return True
        else:
            return False

if __name__ == '__main__':
    so = Solution()
    print so.palindromeNumber(11)

