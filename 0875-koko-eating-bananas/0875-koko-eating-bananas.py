import math

class Solution(object):
    def minEatingSpeed(self, piles, h):

        left = 1

        right = max(piles)

        res = right

        
        while left <= right:
            mid = ( left + right ) // 2  

            total = 0
            for p in piles:
                total += math.ceil(float( p ) / mid )

            if total > h:
                left = mid + 1
            else:
                res = mid
                right = mid -1     

        return res



            

            