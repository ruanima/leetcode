# -*- coding:utf-8 -*-


# English:
# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# Example 1:
# Input: 4 Output: 2
# Example 2:
# Input: 8 Output: 2 Explanation: The square root of 8 is 2.82842..., and since   the decimal part is truncated, 2 is returned.
#
# 中文:
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 示例 1:
# 输入: 4 输出: 2
# 示例 2:
# 输入: 8 输出: 2 说明: 8 的平方根是 2.82842...,   由于返回类型是整数，小数部分将被舍去。


#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (34.46%)
# Total Accepted:    31K
# Total Submissions: 87.6K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left < right:
            mid = (left + right) >> 1
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        if left ** 2 == x:
            return left
        return left - 1

    def mySqrt_v1(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        ret = 0
        while left <= right:
            mid = (left + right) // 2
            # print(mid)
            if mid ** 2 < x:
                left = mid + 1
            elif x < mid ** 2:
                right = mid - 1
            else:
                ret = mid
                break
        else:
            ret = left - 1
        return ret

if __name__ == "__main__":
    s = Solution().mySqrt(8)
    print(s)
    s = Solution().mySqrt(9)
    print(s)
    s = Solution().mySqrt(0)
    print(s)



