class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        n_islands = 0
        queue = []

        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == "1":
                    n_islands += 1
                    queue.append((r, c))
                    grid[r][c] = "0"
                    while queue:
                        _r, _c = queue.pop(0)
                        for x, y in [
                            (_r + 1, _c),
                            (_r - 1, _c),
                            (_r, _c + 1),
                            (_r, _c - 1),
                        ]:
                            if 0 <= x < n_row and 0 <= y < n_col and grid[x][y] == "1":
                                queue.append((x, y))
                                grid[x][y] = "0"
        return n_islands
