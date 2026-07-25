import collections
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        
        graph = collections.defaultdict(list)

        for t in times:
            graph[t[0]].append((t[1], t[2]))

        minheap = []

        visited = set()

        time = []
        minheap = [( 0, k)]
        while minheap:
        
            w, v = heapq.heappop(minheap)

            if v in visited:
                continue

            visited.add( v )
            time.append(w)

            for   v1, w1 in graph[v]:
                heapq.heappush(minheap, (w1 + w, v1))

        if len( visited ) != n:
            return -1
        return max(time)


