# -*- coding:utf-8 -*-


# English:
# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
# Example 1:
# Input: amount = 5, coins = [1, 2, 5] Output: 4 Explanation: there are four ways to make up the amount: 5=5 5=2+2+1 5=2+1+1+1 5=1+1+1+1+1
# Example 2:
# Input: amount = 3, coins = [2] Output: 0 Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
# Input: amount = 10, coins = [10] Output: 1
# Note:
# You can assume that
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
#
# 中文:
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
# 示例 1:
# 输入: amount = 5, coins = [1, 2, 5] 输出: 4 解释: 有四种方式可以凑成总金额: 5=5 5=2+2+1 5=2+1+1+1 5=1+1+1+1+1
# 示例 2:
# 输入: amount = 3, coins = [2] 输出: 0 解释: 只用面额2的硬币不能凑成总金额3。
# 示例 3:
# 输入: amount = 10, coins = [10] 输出: 1
# 注意:
# 你可以假设：
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数


#
# @lc app=leetcode.cn id=518 lang=python
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (41.52%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 4.4K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
#
#
#
#
#
#
# 示例 1:
#
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# 示例 2:
#
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#
#
# 示例 3:
#
# 输入: amount = 10, coins = [10]
# 输出: 1
#
#
#
#
# 注意:
#
# 你可以假设：
#
#
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
#
#
#


class Solution(object):
    def change(self, amount, coins):
        # 以amount=10, coins=[2,3] 为例
        dp = [0] * (amount + 1)    # dp[x]: 拼成x的组合数
        dp[0] = 1   # 要凑成0, 只有一种情况
        for coin in coins:
            for i in range(amount - coin + 1):   # 0, 1, ... 8
                if dp[i]:
                    dp[i + coin] = dp[i + coin] + dp[i]   # 用这个coin的情况 + 不用这个coin的情况
        return dp[amount]

if __name__ == "__main__":
    s = Solution().change(amount = 10, coins = [1, 2, 5])
    print(s)

