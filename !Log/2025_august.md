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
