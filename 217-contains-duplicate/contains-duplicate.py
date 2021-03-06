# -*- coding:utf-8 -*-


# English:
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# Example 1:
# Input: [1,2,3,1] Output: true
# Example 2:
# Input: [1,2,3,4] Output: false
# Example 3:
# Input: [1,1,1,3,3,4,3,2,4,2] Output: true
#
# 中文:
# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
# 示例 1:
# 输入: [1,2,3,1] 输出: true
# 示例 2:
# 输入: [1,2,3,4] 输出: false
# 示例 3:
# 输入: [1,1,1,3,3,4,3,2,4,2] 输出: true


#
# @lc app=leetcode.cn id=217 lang=python
#
# [217] 存在重复元素
#
# https://leetcode-cn.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (46.04%)
# Total Accepted:    48.8K
# Total Submissions: 102.6K
# Testcase Example:  '[1,2,3,1]'
#
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: true
#
# 示例 2:
#
# 输入: [1,2,3,4]
# 输出: false
#
# 示例 3:
#
# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true
#
#

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) != len(nums):
            return True
        return False

