class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unique = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):
            # Keep shrinking from the left
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
                
            #  safe to add the new character
            unique.add(s[right])
            
            # Record the max window size
            longest = max(longest, right - left + 1)
            
        return longest
