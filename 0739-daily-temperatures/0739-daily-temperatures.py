class Solution(object):
    def dailyTemperatures(self, temperatures):
        
        temps = []
        res = [0] * len(temperatures)

        for j, t in enumerate(temperatures):

            
            while temps and t >  temperatures[temps[-1]]:

                i = temps.pop()

                res[i] = j - i
                
            temps.append(j)    
        return res
                




            

                


            
        