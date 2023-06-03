"""
A sliding window is a virtual window in an (alternatively a subarray).
It has a start and an end (left limit and right limit).
We need to find all such substrings in which there is no repeating characters.

A brute force solution would be to loop over all subarrays and check if there are
any duplicates in that window. If no, count its length and keep the maximum.
Since there are O(n^2) number of subarrays in an array, its time complexity would be 
O(n^2)

We can do better using sliding window approach.

---------------------------------------------------------------
Loop invariants
1) We can keep a left and right limit at any given point of time such all the elements between
   left to (right - 1) pointer would be unique.

2) We could keep a memory hash to remember which elements we have seen upto that point and at
   which position it was seen recently.
---------------------------------------------------------------


Right pointer would keep on increasing and exploring new elements.
If we encounter any element that we have already seen and is in the window,
it would violate our first loop invariant. To get free of the violation, we will set
left pointer to one step ahead of where the duplicate element is in the window.

For example:

abcacb

Initiallly:

Data structure:
    res = 0
    left = 0
    right = 0
    memory_hash = {}

right pointer encounters a
We update memory_hash and increment right.
And execute this to update res
res = max(res, r - l)

Step 1:
Data structure:
    res = 1
    left = 0
    right = 1
    memory_hash = {a: 0}

right pointer encounters b
We update memory_hash and increment right.
And execute this to update res
res = max(res, r - l)

    
Step 2:
Data structure:
    res = 2
    left = 0
    right = 2
    memory_hash = {a: 0. b: 1}

right pointer encounters c
We update memory_hash and increment right.
And execute this to update res
res = max(res, r - l)

Step 3:
Data structure:
    res = 3
    left = 0
    right = 3
    memory_hash = {a: 0. b: 1, c: 2}

Right pointer encounters a, again!
Now if we increment right pointer, loop invariant 1 would be violated.
We will instead increment left, so that it is followed.
The simple idea is to set left to one step ahead of where we have seen a last.
So, we set left to 1.
Update memory hash accordingly and increment right by one.
And execute this to update res
res = max(res, r - l)


Step 4:
Data structure:
    res = 3
    left = 1
    right = 4
    memory_hash = {a: 3. b: 1, c: 2}

We encounter c next, the steps are the same as step 3.
We set left to one ahead of where we saw c last (as per memory_hash), i.e. set left to 3.
Update memory_hash accordingly and move right by one.
And execute this to update res
res = max(res, r - l)


Step 5:
Data structure:
    res = 3
    left = 3
    right = 5
    memory_hash = {a: 3. b: 1, c: 4}

Now, we see b again.
In these case though, adding b to our window would now violate loop invariant 1.

The rough visualization below suggests that the window contains a anc c (Note that window ends
right - 1).

0   1   2   3   4   5
a   b   c   a   c   b
            l       r

Although there is an entry for b in the memory hash.
But since the position of b is smaller than left, we can conclude that it is not in the window!
So, we just increment right pointer by one and update memory_hash to now include b.
And execute this to update res
res = max(res, r - l)
And now, right goes out of bounds so we stop execution and return res.


Finally:
Data structure:
    res = 3
    left = 3
    right = 6
    memory_hash = {a: 3. b: 5, c: 4}

res = 3, So, our output is also 3!
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = res = 0
        memory = {}
        while(r < len(s)):
            # Character at right's position should either be
            # 1) not in memory_hash or
            # 2) be at position less than left pointer (So that it is out of the window)
            if(s[r] in memory and l <= memory[s[r]]):
                l = memory[s[r]] + 1
                memory[s[r]] = r
                r += 1
            else:
                memory[s[r]] = r
                r += 1
                res = max(res, r - l)
        return res


