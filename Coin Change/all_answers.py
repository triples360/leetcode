class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        self.res = 0
        self.master_res = []
        self.master_nums = []
        self.nums = []
        def aux(i, amt):
            print(f"aux({i}, {amt})")
            if(amt == 0):
                self.master_res.append(self.res)
                self.master_nums.append(self.nums[:])
                return 
            if(i >= len(coins)):
                return -1
            if(amt - coins[i] < 0):
                # print(f"Calling for {i + 1}, {amt}")
                aux(i + 1, amt)
            else:
                self.res += 1
                # print(f"Incremented res to {self.res}")
                self.nums.append(coins[i])
                aux(i, amt - coins[i])
                self.res -= 1
                self.nums.pop()
                aux(i + 1, amt)
                # if(tmp_ans == -1):
                #     self.res -= 1
                #     # print(f"Decremented res to {self.res}")
                #     self.nums.pop()
                #     aux(i + 1, amt)
                # else:
                #     return tmp_ans
                
        aux(0, amount)
        print(self.master_res)
        print(self.master_nums)
        return self.res
