# -*- coding:utf-8 -*-


# English:
# Given an integer array, find three numbers whose product is maximum and output the maximum product.
# Example 1:
# Input: [1,2,3] Output: 6
# Example 2:
# Input: [1,2,3,4] Output: 24
# Note:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
#
# 中文:
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 示例 1:
# 输入: [1,2,3] 输出: 6
# 示例 2:
# 输入: [1,2,3,4] 输出: 24
# 注意:
# 给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


#
# @lc app=leetcode.cn id=628 lang=python
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (44.25%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 14.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
#
# 示例 1:
#
#
# 输入: [1,2,3]
# 输出: 6
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4]
# 输出: 24
#
#
# 注意:
#
#
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
#
#
#
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = []
        p = []
        for i in nums:
            if i < 0:
                n.append(i)
            else:
                p.append(i)
        n.sort()
        p.sort()
        if len(p) >= 3:
            if len(n) >= 2:
                return max(p[-3] * p[-2] * p[-1], p[-2] * p[-1] * n[-1], p[-1] * n[0] * n [1])
            return p[-3] * p[-2] * p[-1]
        if len(p) == 2:
            if len(n) >= 2:
                return max(p[-2] * p[-1] * n[-1], p[-1] * n[0] * n [1])
            return  p[-2] * p[-1] * n[-1]
        if len(p) == 1:
            return  p[-1] * n[0] * n[1]
        if len(p) == 0:
            return n[-3] * n[-2] * n[-1]

if __name__ == "__main__":
    s = Solution().maximumProduct([722,634,-504,-379,163,-613,-842,-578,750,951,-158,30,-238,-392,-487,-797,-157,-374,999,-5,-521,-879,-858,382,626,803,-347,903,-205,57,-342,186,-736,17,83,726,-960,343,-984,937,-758,-122,577,-595,-544,-559,903,-183,192,825,368,-674,57,-959,884,29,-681,-339,582,969,-95,-455,-275,205,-548,79,258,35,233,203,20,-936,878,-868,-458,-882,867,-664,-892,-687,322,844,-745,447,-909,-586,69,-88,88,445,-553,-666,130,-640,-918,-7,-420,-368,250,-786])
    print(s)
    s = Solution().maximumProduct([-710,-107,-851,657,-14,-859,278,-182,-749,718,-640,127,-930,-462,694,969,143,309,904,-651,160,451,-159,-316,844,-60,611,-169,-73,721,-902,338,-20,-890,-819,-644,107,404,150,-219,459,-324,-385,-118,-307,993,202,-147,62,-94,-976,-329,689,870,532,-686,371,-850,-186,87,878,989,-822,-350,-948,-412,161,-88,-509,836,-207,-60,771,516,-287,-366,-512,509,904,-459,683,-563,-766,-837,-333,93,893,303,908,532,-206,990,280,826,-13,115,-732,525,-939,-787])
    print(s)

