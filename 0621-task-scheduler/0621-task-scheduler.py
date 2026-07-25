class Solution(object):
    def leastInterval(self, tasks, n):
        
        words = collections.defaultdict(int)

        for t in tasks:
            words[t] += 1

        maxHeap = [-c for c in words.values()]

        heapq.heapify(maxHeap)

        line = collections.deque()

        time = 0
        while maxHeap or line:
            
            time += 1

            if maxHeap:
                cur = heapq.heappop(maxHeap)
                if cur + 1 != 0:
                    line.append((cur + 1, time + n))


            if line and line[0][1] == time:
                f, t = line.popleft()
                heapq.heappush(maxHeap, f)


        return time