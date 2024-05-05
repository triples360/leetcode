class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = 0
        self.master_res = float("inf")
        def aux(i, amt):
            if(amt == 0):
                self.master_res = min(self.master_res, self.res)
                return
            if(i >= len(coins)):
                return -1
            if(amt - coins[i] < 0):
                # print(f"Calling for {i + 1}, {amt}")
                aux(i + 1, amt)
            else:
                self.res += 1
                # print(f"Incremented res to {self.res}")
                aux(i, amt - coins[i])
                self.res -= 1
                aux(i + 1, amt)
                # if(tmp_ans == -1):
                #     self.res -= 1
                #     # print(f"Decremented res to {self.res}")
                #     self.nums.pop()
                #     aux(i + 1, amt)
                # else:
                #     return tmp_ans
                
        aux(0, amount)
        if(self.master_res == float("inf")):
            return -1
        return self.master_res
