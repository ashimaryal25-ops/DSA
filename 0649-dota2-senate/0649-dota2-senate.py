class Solution(object):
    def predictPartyVictory(self, senate):
        rad = deque()

        dire = deque()
        n = len(senate)
        count  = 1
        for s in senate:
            
            if s == "R":
                rad.append(count)
            else:
                dire.append(count)
            count = count + 1



        while rad and dire: 

            index1 = rad.popleft()

            index2 = dire.popleft()

            if index1 < index2:
                rad.append(index1 + n)
            else:
                dire.append(index2 + n) 

        if rad:
            return "Radiant"
        else:
            return "Dire"    

            
            
