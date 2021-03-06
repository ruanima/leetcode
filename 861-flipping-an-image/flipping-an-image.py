# -*- coding:utf-8 -*-


# English:
# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
# Example 1:
# Input: [[1,1,0],[1,0,1],[0,0,0]] Output: [[1,0,0],[0,1,0],[1,1,1]] Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j]
# <=
# 1
#
# 中文:
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
# 示例 1:
# 输入: [[1,1,0],[1,0,1],[0,0,0]] 输出: [[1,0,0],[0,1,0],[1,1,1]] 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]； 然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
# 示例 2:
# 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]] 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]] 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]； 然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 说明:
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1


#
# @lc app=leetcode.cn id=832 lang=python
#
# [832] 二叉树剪枝
#
# https://leetcode-cn.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (68.80%)
# Total Accepted:    12.9K
# Total Submissions: 18.3K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
#
# 水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
#
# 反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
#
# 示例 1:
#
#
# 输入: [[1,1,0],[1,0,1],[0,0,0]]
# 输出: [[1,0,0],[0,1,0],[1,1,1]]
# 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
# ⁠    然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#
#
# 示例 2:
#
#
# 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
# ⁠    然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#
# 说明:
#
#
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1
#
#
#
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A = [row[::-1] for row in A]

        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A

if __name__ == "__main__":
    d = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    s = Solution().flipAndInvertImage(d)
    print(s)

