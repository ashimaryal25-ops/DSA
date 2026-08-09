class Solution(object):
    def mergeTriplets(self, triplets, target):
        best = [0, 0, 0]

        for trip in triplets:

            # skip triplets that overshoot target anywhere
            if (trip[0] > target[0] or
                trip[1] > target[1] or
                trip[2] > target[2]):
                continue

            # safe triplet, merge with max
            best[0] = max(best[0], trip[0])
            best[1] = max(best[1], trip[1])
            best[2] = max(best[2], trip[2])

        return best == target
        