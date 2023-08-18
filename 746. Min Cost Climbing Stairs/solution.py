#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#


# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(2, len(cost)):  # -3 to -len(cost)
            cost[~i] += min(cost[~i + 1], cost[~i + 2])
        return min(cost[0], cost[1])


# @lc code=end
