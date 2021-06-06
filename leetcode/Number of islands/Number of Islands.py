class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def walk(grid, n, m, round, max_n = len(grid) - 1, max_m = len(grid[0]) - 1):
            if n > max_n or n < 0 or m > max_m or m < 0:
                return round

            if grid[n][m] == "0":
                return round
            elif grid[n][m] == "2":
                return round
            elif grid[n][m] == "1":
                grid[n][m] = "2"
                round += 1
            walk(grid, n + 1, m, round)
            walk(grid, n - 1, m, round)
            walk(grid, n, m + 1, round)
            walk(grid, n, m - 1, round)

        max_n = len(grid)
        max_m = len(grid[0])
        island = 0
        for x in range(max_n):
            for y in range(max_m):
                round = 0
                round = walk(grid, x, y, round)
                if round != 0:
                    island += 1
        return island, grid

grid = [["1","0","1","1","0","1","1"]]
sol = Solution()
ans = sol.numIslands(grid)
print(ans)