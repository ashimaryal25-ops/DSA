class Solution(object):
    def partitionLabels(self, s):
        last = {}

        # store last index of every character
        for i, c in enumerate(s):
            last[c] = i

        res = []
        start = 0
        end = 0

        for i, c in enumerate(s):
            # current partition must reach at least
            # this character's last occurrence
            end = max(end, last[c])

            # safe to cut here
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res