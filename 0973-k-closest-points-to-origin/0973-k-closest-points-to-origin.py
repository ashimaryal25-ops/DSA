import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, [x, y]))

        res = []

        for _ in range(k):
            dist, point = heapq.heappop(heap)
            res.append(point)

        return res