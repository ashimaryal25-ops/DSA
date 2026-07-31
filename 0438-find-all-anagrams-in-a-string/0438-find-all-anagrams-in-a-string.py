class Solution(object):
    def findAnagrams(self, s, p):
        res = []

        if len(s) < len(p):
             return res

        char_map = collections.defaultdict(int)
        window_map = collections.defaultdict(int)

        # making the map

        for c in p:

            char_map[c] += 1


        #initial dict for initial window of s2:
        
        for i in range(len(p)):

            window_map[s[i]] += 1
            
        
        if char_map == window_map:
            res.append(0)


        left = 0
        right = len(p)

        
        while right < len(s) :

            window_map[s[left]] -= 1

            if window_map[s[left]] == 0:
                del window_map[s[left]]

            window_map[s[right]] += 1    

            if char_map == window_map:
                res.append(left + 1)
            
            left = left + 1

            right = right + 1


        return res