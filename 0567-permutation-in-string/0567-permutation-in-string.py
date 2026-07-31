class Solution(object):
    def checkInclusion(self, s1, s2):
        
        if len(s1) > len(s2):
            return False

        if not s1:
            return True

        if not s2:
            return False

        char_map = collections.defaultdict(int)
        window_map = collections.defaultdict(int)

        # making the map

        for c in s1:

            char_map[c] += 1


        #initial dict for initial window of s2:
        
        for i in range(len(s1)):

            window_map[s2[i]] += 1
            
        
        if char_map == window_map:
            return True


        left = 0
        right = len(s1)

        
        while right < len(s2) :

            window_map[s2[left]] -= 1

            if window_map[s2[left]] == 0:
                del window_map[s2[left]]

            window_map[s2[right]] += 1    

            if char_map == window_map:
                return True
            
            left = left + 1

            right = right + 1


        return False

        