class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count_numbers(pref1, pref2):
            numbers = 0
            while pref1 <= n:
                numbers += min(n + 1, pref2) - pref1
                pref1 *= 10
                pref2 *= 10

            return numbers

        curr = 1
        k -= 1

        while k: 

            # count_numbers counts all the numbers which have the prefix 'curr'
            # and are smaller than 'n' (except 'curr' itself).
            numbers_under_curr = count_numbers(curr*10, 10*(curr + 1))

            # The node with value 'curr' should have all the numbers that have prefix 'curr'
            # by the definition of trie.
            # So, 'numbers_under_curr' tells us how many numbers are under the node valued 'curr'.
            # If this is greater than k, we know that the needed element 'k' is below the node 'curr'
            # We travel down below to 'curr * 10' which is the first child of node 'curr' by the definition
            # of trie.
            if numbers_under_curr >= k:
                curr *= 10
            else:
                # If 'numbers_under_curr' is smaller than k, then we know that the needed element 'k' is not under
                # node 'curr'. But it may be under curr + 1, so we increment curr to look for it there. We also
                # reduce k by 'numbers_under_curr' since those many elements we skip over by skipping the entire
                # subtree rooted at node 'curr'
                curr += 1
                k -= numbers_under_curr
            k -= 1

        return curr
