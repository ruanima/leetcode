# -*- coding:utf-8 -*-


# English:
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.
# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.
# Given two (axis-aligned) rectangles, return whether they overlap.
# Example 1:
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3] Output: true
# Example 2:
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1] Output: false
# Notes:
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
#
# 中文:
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
# 给出两个矩形，判断它们是否重叠并返回结果。
# 示例 1：
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3] 输出：true
# 示例 2：
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1] 输出：false
# 说明：
# 两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
# 矩形中的所有坐标都处于 -10^9 和 10^9 之间。


#
# @lc app=leetcode.cn id=836 lang=python
#
# [836] 矩形重叠
#
# https://leetcode-cn.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (39.34%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 6.4K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
#
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
#
# 给出两个矩形，判断它们是否重叠并返回结果。
#
# 示例 1：
#
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
#
#
# 示例 2：
#
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
#
#
# 说明：
#
#
# 两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
# 矩形中的所有坐标都处于 -10^9 和 10^9 之间。
#
#
#
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2
        return not (a1 >= x2 or x1 >= a2 or b1 >= y2 or y1 >= b2)

if __name__ == "__main__":
    s = Solution()
    print(s.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
    s = Solution()
    print(s.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))


