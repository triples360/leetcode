class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = 1
        res = -float("inf")
        # Go left to right
        for i in range(len(nums)):
            prod = nums[i] * prod
            res = max(res, prod)
            # Re-evaluate result from next element by setting prod to 0.
            if(prod == 0):
                prod = 1
        
        prod = 1
        # Go right to left
        for i in range(len(nums) - 1, -1, -1):
            prod = nums[i] * prod
            res = max(res, prod)
            # Re-evaluate result from next element by setting prod to 0.
            if(prod == 0):
                prod = 1
        
        return res
