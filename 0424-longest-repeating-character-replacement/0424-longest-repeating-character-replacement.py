class Solution(object):
    def characterReplacement(self, s, k):
        count = collections.defaultdict(int)
        res = 0
        left = 0
        maxf = 0

        for right in range(len(s)):
            # Add the new character to our frequency map
            count[s[right]] += 1
            
            # Track the highest frequency of a single character in the window
            maxf = max(maxf, count[s[right]])

            # If the window breaks the rules, slide the left pointer forward
            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            # Record the biggest valid window we've seen
            res = max(res, right - left + 1)

        return res
        