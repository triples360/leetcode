"""
One trick here is to notice that if you substract prices[i] - price[i - 1]
Like the code snippet below would do.

diff = []
for i in range(2, len(prices)):
    diff.append(prices[i] - prices[i - 1])


It (diff array) would essentially give us the changes from one point to another.
For example, if you sum diff from index i to index j, it gives us the profit obtained
by buying at i and selling at j.

This way the problem reduces to the 'Maximum subarray sum' problem.

We really don't need to calculate the diff array, we could just use prices[i] - prices[j]
on demand since it is required only for each i. This saves us space!

Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        acc_sum = 0
        for i in range(1, len(prices)):
            acc_sum += (prices[i] - prices[i - 1])
            if(acc_sum < 0):
                acc_sum = 0
            else:
                res = max(res, acc_sum)
        return res



