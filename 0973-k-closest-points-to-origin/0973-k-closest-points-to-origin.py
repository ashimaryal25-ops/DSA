import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = x * x + y * y

            # Python heapq is a min-heap,
            # so negate distance to simulate a max-heap
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        while heap:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res