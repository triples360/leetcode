"""
Since this problem asks us to look for substrings, we can look into the sliding window
technique to approach this problem. 

The problem requires us to find an anagram substring of s1 inside of s2.
Of course, the required anagram would be of size equal to s1. Therefore,
the window will be of constant length in this problem (length of s1)

An obvious brute force solution is to get the frequency hash for s1, then get all
substrings of s2 of length = len(s1), and see of their frequency hash equals required
frequency hash.

This approach works but is not optimal, we have to traverse the substring again and again
to construct its frequency hash.

We can apply one simple trick to the above solution to make it more efficient.
We know we need to slide the window one step each time, left moves ahead along with right
to keep the window size same. We can decrement left character's occurences by one and
increment right's by one. This way we don't have to go through the substrings again.

Also, we can keep track of how many characters are matching in the window and required freq
hash. Each time our window moves ahead, we can update the number of matches in the hashes.
Whenever the number of matches equal 26, it means the window and the frequency hash are equal,
which means the window and s1 are anagrams.

The window will follow two loop invariants
1) Window size is equal to the size of the string s1.
2) window_hash is a hash which stores the frequency of all characters in the window.
3) 'matches' is an integer which equals how many characters have the same frequency as
    the required_hash
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # required_hash hash and the window_hash hash to store character frequencies of 
        # s1 (required_hash) and the window_hash in 
        required_hash = {}
        window_hash = {}

        # matches variable stores how many characters have the same freq i.e. how many
        # characters match the freq in both hashes
        matches = 0
        if(len(s1) > len(s2)):
            return False
        
        # Enter all characters in the hashes
        for c in "abcdefghijklmnopqrstuvwxyz":
            required_hash[c] = 0
            window_hash[c] = 0
        
        # Build required_hash
        s1l = 0
        while(s1l < len(s1)):
            required_hash[s1[s1l]] += 1
            s1l += 1
        
        # Build initial window_hash for the first len(s1) characters
        left = right = 0
        while(right < len(s1)):
            window_hash[s2[right]] += 1
            right += 1
        
        # Get how many matches we have initially
        matches = 0
        for char in required_hash:
            if(required_hash[char] == window_hash[char]):
                matches += 1
        
        if(matches == 26):
            return True

        # Keep on the sliding the window till it is out of bounds
        while(right < len(s2)):

            # Increment the freq of s2[right] by 1, check if the matches variable
            # need to decremented or incremented
            window_hash[s2[right]] += 1
            if(window_hash[s2[right]] == required_hash[s2[right]]):
                matches += 1
            elif(window_hash[s2[right]] - 1 == required_hash[s2[right]]):
                matches -= 1
            
            # Decrement the freq of s2[left] by 1, check if the matches variable
            # need to decremented or incremented
            window_hash[s2[left]] -= 1
            if(window_hash[s2[left]] == required_hash[s2[left]]):
                matches += 1
            if(window_hash[s2[left]] + 1 == required_hash[s2[left]]):
                matches -= 1
            
            # If all frequencies match, its an anagram as we needed, return true
            if(matches == 26):
                return True
            right += 1
            left += 1
        
        return False
        

