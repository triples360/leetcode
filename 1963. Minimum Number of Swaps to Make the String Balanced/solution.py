"""
To solve this problem first we remove all valid_pairs from the strings.
How?
    We go just how we'd normally go to validate a string with just one flourish.
    Whenever we see a ']' and stack is empty, we ignore it and move to the next element.

    Otherwise, we go as usual. We see '[', we push it.
    We see ']' and stack isn't empty we pop the stack and add 1 to valid_pairs variable.


Now, we'll be left with string of the form:
...]]]][[[[...

We just gotta solve for these remaining pairs with swapping.
Let's look at the middle of the remaining string. Say there are atleast 2 pairs.
Then the middle would be like this
...]][[...
To balance the middle 2 pairs, we don't have to make 2 swaps like first with last and the
two middle ones with each other.
0 1 2 3
] ] [ [

Swap 0 and 3
0 1 2 3
[ ] [ ]

Swap 1 and 2
0 1 2 3
[ [ ] ]

This is actually a longer way.
We could simply swap 0 and 2 like below

0 1 2 3
] ] [ [

Swap 0 and 3
0 1 2 3
[ ] [ ]

So, just one swap gets the job done for the middle 2 pairs. We can remove these pairs and now have to only
work with remaning pairs.

For example if we have ]]]][[[[

0 1 2 3 4 5 6 7
] ] ] ] [ [ [ [

Let's take the middle 2 pairs - from index 2 to 5 inclusive.
Swap 2 and 5.
0 1 2 3 4 5 6 7
] ] [ ] [ ] [ [

Since the subarray from 2 to 5 is now balance, the remaning string is:
0 1 6 7
] ] [ [

Swap 0 and 7 and we're done.
0 1 6 7
[ ] [ ]

In conlusion, we only need 1 swap for 2 pairs.
Therefore, we can come up with the below formula because 2 pairs require one swap.

number of swaps = remaning_pairs / 2

Also, when there is just 1 pair, we'll still require 1 swap so we ceil it.

Final formula becomes:
number of swaps = ceil(remaning_pairs / 2)

"""

class Solution:
    def minSwaps(self, s: str) -> int:

        # We'll remove the pairs which are valid.
        # For this we use the normal stack approach, the below stack variable keeps
        # track of how many '[' we've seen so far
        stack = 0
        valid_pairs = 0
        for brack in s:
            if(brack == '['):
                stack += 1
            else:
                if(stack):
                    valid_pairs += 1
                    stack -= 1
        
        remaining_pairs = len(s) // 2 - valid_pairs
        return math.ceil(remaining_pairs/2)

        return res
