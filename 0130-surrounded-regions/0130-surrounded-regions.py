class Solution(object):
    def solve(self, board):
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        seen = set()

        def dfs(r, c, cluster):
            # Out of bounds = reached the boundary / unsafe -> return False
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            #  Wall = blocked / safe -> return True
            if board[r][c] == 'X':
                return True

            # Already visited in this component = safe -> return True
            if (r, c) in seen:
                return True

            # Mark as visited and add to current cluster
            seen.add((r, c))
            cluster.append((r, c))

            # Check all 4 directions explicitly
            up = dfs(r - 1, c, cluster)
            down = dfs(r + 1, c, cluster)
            left = dfs(r, c - 1, cluster)
            right = dfs(r, c + 1, cluster)

            # Safe only if all 4 directions are sealed
            return up and down and left and right

        # Iterate over the entire board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in seen:
                    cluster = []
                    # If the entire cluster is surrounded, flip all its cells
                    if dfs(r, c, cluster):
                        for cr, cc in cluster:
                            board[cr][cc] = 'X'
    







        