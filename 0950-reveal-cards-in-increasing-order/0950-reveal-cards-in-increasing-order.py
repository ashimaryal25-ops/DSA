from collections import deque

class Solution(object):
    def deckRevealedIncreasing(self, deck):
        sorted_deck = sorted(deck)

        res_deck = [0] * len(deck)
        q = deque(range(len(deck)))

        for card in sorted_deck:
            # This position will be revealed next
            index = q.popleft()
            res_deck[index] = card

            # Move the next position to the back
            if q:
                q.append(q.popleft())

        return res_deck
                


              
        