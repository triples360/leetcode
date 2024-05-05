class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = 0
        self.master_res = float("inf")
        memory = {}
        def aux(i, amt):
            # print(f"aux({i}, {amt})")
            if((i, amt) in memory):
                print(f"({i}, {amt}) was found to be in memory")
                print(f"Two answers {self.master_res}, {self.res + memory[(i, amt)]} from memory")
                self.master_res = min(self.master_res, self.res + memory[(i, amt)])
                return memory[(i, amt)]
            if(amt == 0):
                print(f"Two answers {self.master_res}, {self.res}")
                self.master_res = min(self.master_res, self.res)
                return self.res
            if(i >= len(coins)):
                return float("inf")
            if(amt - coins[i] < 0):
                # print(f"Calling for {i + 1}, {amt}")
                tmp_ans = aux(i + 1, amt)
                memory[(i, amt)] = tmp_res
                return tmp_ans
            else:
                self.res += 1
                # print(f"Incremented res to {self.res}")
                choose = aux(i, amt - coins[i])
                self.res -= 1
                dont = aux(i + 1, amt)
                memory[(i, amt)] = min(choose, dont)
                # if(tmp_ans == -1):
                #     self.res -= 1
                #     # print(f"Decremented res to {self.res}")
                #     self.nums.pop()
                #     aux(i + 1, amt)
                # else:
                #     return tmp_ans
                return memory[(i, amt)]
                
        aux(0, amount)
        if(self.master_res == float("inf")):
            return -1
        return self.master_res
