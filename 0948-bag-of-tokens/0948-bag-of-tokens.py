class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        

        sorted_tokens = sorted(tokens)

        curPower = power

        score = 0


        # two pointers on a sorted list = deque

        #facedown u would want to pick the max fromt the token array from the token array so we can probebly use maxheap to put the max at the left. for faceup goal is to maximise the score so youd want to strategeciclly choose the lowest tokens from the tokens array.

        left = 0

        right = len(sorted_tokens) - 1

        # When left == right, there is still 1 token left. If you have enough power, can and should buy it
        while left <= right:

            if sorted_tokens[left] <= curPower:
                curPower -= sorted_tokens[left]
                score += 1
                left = left + 1
            elif score > 0 and right-left+1 > 1:
                curPower += sorted_tokens[right]
                score -= 1    
                right = right - 1
            else:
                break    
        return score

        