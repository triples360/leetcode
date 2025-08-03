# Greatest common divisor traversal
Link: https://leetcode.com/problems/greatest-common-divisor-traversal/submissions/1717503732

 - GCD of two numbers basically check if there are any common primes between the prime factorization of the two numbers. All those common numbers multiplied together is the GCD.

 - Question says that if there are any common primes (gcd > 1) then you can travel between the nodes.

Solution approach:
1) Union find
2) Two elements having at least on common prime in their factors can travel between each other.
For example:
6 and 8 can travel between each other.
Other way to think about this is:

Since 6 can travel to 2 (one of its prime factors) and 8 can also (again a factor).
They can travel to each other through 2.

3) Create a node for all primes less than max(nums) and create a node for all nums.
4) Create the sieve of erasthothenes.
5) Get the factors from the sieve for each number and union the nodes of the factor and num.

Notes: Union must always have the primes as parent. So, write union(n1, n2) such that if rank1 == rank2 then n1 is the parent. Send prime first. This way only primes become the parents (representatives in union find).

Use union by rank and path compression.

6) If all nums returns the same find(num) return true; otherwise false.

# 236. Lowest Common Ancestor of a Binary Tree

Think from root's perspective:

If I am null, I'll return null.

If I am either p or q, I'll return myself.
This is because root is either
- The LCA of the whole, for example if root is p and q lies in its subtree and vice versa as p and q are not special and could be exchanged without having any impact on the solution.
 - Or not (if root is p and q lies in the other child of its ancestors). In both cases, we return root.

Call both the children recursively to get their lca, left and right.

If both left and right are non-null, then that must mean I am the LCA; return root.

If either left or right is non-null, return it.

If both are null, return null.

# 2096. Step-By-Step Directions From a Binary Tree Node to Another

Observe the fact that both source and destination must be present in the subtree rooted at the LCA node. Also, the path from source to destination must pass from  the LCA node.

1) Find out the LCA node as in [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/submissions/1588965793/).

2) Find out the path from LCA to startValue node.

3) Find out the path from LCA to destValue node.

4) Replace the path to startValue with all 'U's and append the destValue node. 

# 1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/submissions/1721625768/

 - We can find out all the predecessors of a string, say abc, easier than its successors.
abc --> ab, ac, bc
We just delete one character and keep others as is.

 - The string chain must have increasing lengths of strings as you go through the chain.
 For example: a -> ba -> cba -> cbfa
 Each string in the chain has length one more than its predecessor.

 - The problem has optimal substructure. 
    Lets say we have a string s in the list and T(s) denotes the longest string chain whose last element is s.

    T(s) = T(p) + 1 for all p present in the input

 - It is also quite simple to see the problem has overlapping subproblems as well.

 - So we can employ Dynamic Programming.


1) Sort the input string in buckets of their lengths.
    We could also sort the strings based on their lengths, but I think it is more optimal to sort them in buckets of their length in this case because the lengths are in the [1, 16] as given in the constraints and sorting in buckets becomes linear this way.

2) Go through the buckets 1 to 16 one by one and you use the equation above to build bottom up.

3) Return the max value of the memory DP hash.
