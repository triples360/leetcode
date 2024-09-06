class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        remaining_points = (mean * (n + len(rolls))) - sum(rolls)
        if(remaining_points > 6 * n or remaining_points < n):
            return []
        distribution_mean = remaining_points // n
        mod = remaining_points % n

        res = [distribution_mean] * n
        for i in range(mod):
            res[i] += 1
        
        return res
