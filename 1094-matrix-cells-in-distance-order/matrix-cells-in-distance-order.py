# -*- coding:utf-8 -*-


# English:
# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
# Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)
# Example 1:
# Input: R = 1, C = 2, r0 = 0, c0 = 0 Output: [[0,0],[0,1]] Explanation: The distances from (r0, c0) to other cells are: [0,1]
# Example 2:
# Input: R = 2, C = 2, r0 = 0, c0 = 1 Output: [[0,1],[0,0],[1,1],[1,0]] Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2] The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
# Example 3:
# Input: R = 2, C = 3, r0 = 1, c0 = 2 Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]] Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2,2,3] There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
# Note:
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C
#
# 中文:
# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
# 另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
# 返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）
# 示例 1：
# 输入：R = 1, C = 2, r0 = 0, c0 = 0 输出：[[0,0],[0,1]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
# 示例 2：
# 输入：R = 2, C = 2, r0 = 0, c0 = 1 输出：[[0,1],[0,0],[1,1],[1,0]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2] [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
# 示例 3：
# 输入：R = 2, C = 3, r0 = 1, c0 = 2 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]] 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3] 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
# 提示：
# 1 <= R <= 100
# 1 <= C <= 100
# 0 <= r0 < R
# 0 <= c0 < C


#
# @lc app=leetcode.cn id=1030 lang=python
#
# [1030] 距离顺序排列矩阵单元格
#
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dis_map = {}
        for x in range(0, R):
            for y in range(0, C):
                dis_map[(x, y)] = abs(x-r0) + abs(y-c0)
        return [list(i[0]) for i in sorted(dis_map.items(), key=lambda i: i[1])]

if __name__ == "__main__":
    s = Solution().allCellsDistOrder(R = 1, C = 2, r0 = 0, c0 = 0)
    print(s)
    s = Solution().allCellsDistOrder(R = 2, C = 2, r0 = 0, c0 = 1)
    print(s)
    s = Solution().allCellsDistOrder(R = 3, C = 5, r0 = 2, c0 = 3)
    print(s)



