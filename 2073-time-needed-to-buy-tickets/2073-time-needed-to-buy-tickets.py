class Solution(object):
    def timeRequiredToBuy(self, tickets, k):

        q = deque()

        for i, t  in enumerate(tickets):
            q.append([i, t])

        time = 0

        while True:

             curFront = q.popleft()
             time += 1
             curFront[1] -= 1
             if curFront[1] != 0:
                q.append(curFront)
             if curFront[0] == k and curFront[1] == 0:
                break    
        return time