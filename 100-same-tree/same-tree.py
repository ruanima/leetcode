# -*- coding:utf-8 -*-


# English:
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
# Example 1:
# Input: 1 1 / \ / \ 2 3 2 3 [1,2,3], [1,2,3] Output: true
# Example 2:
# Input: 1 1 / \ 2 2 [1,2], [1,null,2] Output: false
# Example 3:
# Input: 1 1 / \ / \ 2 1 1 2 [1,2,1], [1,1,2] Output: false
#
# 中文:
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 示例 1:
# 输入: 1 1 / \ / \ 2 3 2 3 [1,2,3], [1,2,3] 输出: true
# 示例 2:
# 输入: 1 1 / \ 2 2 [1,2], [1,null,2] 输出: false
# 示例 3:
# 输入: 1 1 / \ / \ 2 1 1 2 [1,2,1], [1,1,2] 输出: false


#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val == q.val:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                    return True
        return False


