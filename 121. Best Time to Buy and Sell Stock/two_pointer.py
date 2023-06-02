"""
A very simple solution to this is the n^2 runtime algorithm.

res = 0
for i in range(len(prices)):
     for j in  range(i + 1, len(prices)):
        res = max(res, prices[j] - prices[i])

There is an O(n) runtime algorithm.
What extra work are we doing in the O(n^2) approach?

Turns out we don't need to check j for all i's.

If prices[i] > prices[j]
    then we could just update i to be equal to j!
    Why?
    If prices[i] is greater than prices[j], then prices coming up ahead of j, lets say k
    would have a higher profit with prices[j] and prices[k] as start and end
    since prices[i] > prices[j]
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        res = 0

        while(right < len(prices)):
            if(prices[left] >= prices[right]):
                left = right
            else:
                res = max(res, prices[right] - prices[left])
            right += 1
        
        return res
