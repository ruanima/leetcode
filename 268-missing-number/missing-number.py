# -*- coding:utf-8 -*-


# English:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Example 1:
# Input: [3,0,1] Output: 2
# Example 2:
# Input: [9,6,4,2,3,5,7,0,1] Output: 8
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#
# 中文:
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
# 示例 1:
# 输入: [3,0,1] 输出: 2
# 示例 2:
# 输入: [9,6,4,2,3,5,7,0,1] 输出: 8
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?


#
# @lc app=leetcode.cn id=268 lang=python
#
# [268] 缺失数字
#
# https://leetcode-cn.com/problems/missing-number/description/
#
# algorithms
# Easy (47.62%)
# Total Accepted:    16.4K
# Total Submissions: 33.4K
# Testcase Example:  '[3,0,1]'
#
# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
# 示例 1:
#
# 输入: [3,0,1]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [9,6,4,2,3,5,7,0,1]
# 输出: 8
#
#
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
#
#
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        tmp = (length * (length+1))/2
        return tmp - sum(nums)


