# -*- coding:utf-8 -*-


# English:
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Example 1:
# Input: 1->1->2 Output: 1->2
# Example 2:
# Input: 1->1->2->3->3 Output: 1->2->3
#
# 中文:
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 示例 1:
# 输入: 1->1->2 输出: 1->2
# 示例 2:
# 输入: 1->1->2->3->3 输出: 1->2->3


# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (44.38%)
# Total Accepted:    19.7K
# Total Submissions: 44.3K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        tmp = []
        node = self
        while node:
            tmp.append(repr(node.val))
            node = node.next
        return ' -> '.join(tmp)

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        ptr = head
        while ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                continue
            ptr = ptr.next
        return head

if __name__ == "__main__":
    l = build_list_node([1,1,2,2,2,3,4,4,6,8])
    print(Solution().deleteDuplicates(l))



