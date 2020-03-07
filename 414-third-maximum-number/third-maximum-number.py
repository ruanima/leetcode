# -*- coding:utf-8 -*-


# English:
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
# Example 1:
#
# Input: [3, 2, 1] Output: 1 Explanation: The third maximum is 1.
# Example 2:
#
# Input: [1, 2] Output: 2 Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
#
# Input: [2, 2, 3, 1] Output: 1 Explanation: Note that the third maximum here means the third maximum distinct number. Both numbers with value 2 are both considered as second maximum.
#
# 中文:
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
# 示例 1:
# 输入: [3, 2, 1] 输出: 1 解释: 第三大的数是 1.
# 示例 2:
# 输入: [1, 2] 输出: 2 解释: 第三大的数不存在, 所以返回最大的数 2 .
# 示例 3:
# 输入: [2, 2, 3, 1] 输出: 1 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。 存在两个值为2的数，它们都排第二。


#
# @lc app=leetcode.cn id=414 lang=python
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (30.60%)
# Total Accepted:    6.4K
# Total Submissions: 20.7K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
#
# 示例 1:
#
#
# 输入: [3, 2, 1]
#
# 输出: 1
#
# 解释: 第三大的数是 1.
#
#
# 示例 2:
#
#
# 输入: [1, 2]
#
# 输出: 2
#
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
#
#
# 示例 3:
#
#
# 输入: [2, 2, 3, 1]
#
# 输出: 1
#
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
#
#
#
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = None
        for i in nums:
            if i in (first, second, third): continue
            if first == None or i >= first:
                first, second, third = i, first, second
            elif second == None or i >= second:
                second, third = i, second
            elif third == None or i >= third:
                third = i
        return third if third is not None else first

