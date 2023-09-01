"""

Problem link:
https://leetcode.com/problems/reverse-nodes-in-k-group/


This problem is one of the type in which a naturally thought out solution suffices.
You should have already done the basic reverse linked list using the three pointer
technique for this one to come to you though.

Basically, we are supposed to reverse the linked list in chunks of k (a given constant).
To think of a very basic solution, we can break the linked list in small chunks of k size each,
then we can just reverse each chunk like we would reverse a linked list. We can set each
connection correctly of the new reversed chunks so that they are in the required order.

And that's it! That's the solution. I personally feel like this is a very natural solution
and if we get a similar problem in real life, we might use this technique there as well.
No tricks or anything!

To implement this solution could be a bit intimidating though, which is probably why it
is classified as hard.

One minor complication is the requirement of this problem to not reverse the last chunk
if it is smaller than size k. For this we will always need to go over the current chunk
size and see if it is size k, if smaller than that we will only attach the links correctly
and halt the program.

We will not go over how to attach the links between the chunks once they are reversed as
it could be easy to come up with with the same natural thinking process.
"""


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Determine head, it would be the kth element or if there are
        # less than k element in the list, then it is the first.

        res = head
        traveller = head
        i = 1

        # The code snippet below will determine the head of the resulatant linked list for us beforehand.
        # This is because we can find out what head would be. Simply, it would be the kth element in 
        # the list. If there are less than k elements in the list, the head stays the same.
        while(traveller and i < k):
            traveller = traveller.next
            i += 1
        if(i == k):
            res = traveller

        three = head
        prevtail = None
        while(three):
            traveller = three
            i = 0 
            # The code snippet below will check if there are atleast k elements in the list ahead.
            # If yes this k elements will form the chunk to be reversed.
            # If no, we halt the problem in the if condition below the while loop, since we are not
            # supposed to reverse the last chunk if it is smaller size than k.
            while(traveller and i < k):
                traveller = traveller.next
                i += 1
            if(i != k):
                if(prevtail):
                    prevtail.next = three
                break
            
            # Once we have atleast k elements in the list ahead, we will use the basic three pointer
            # technique to reverse them.
            one = None
            two = three
            three = two.next
            currtail = two
            i = 1
            while(i < k):
                two.next = one
                one = two
                two = three
                three = three.next
                i += 1
            
            # This below snippet will set the pointers correctly after the reversing.
            two.next = one
            if(prevtail):
                prevtail.next = two
            prevtail = currtail

        return res

