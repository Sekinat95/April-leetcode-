#number of islands. A GRAPH QUESTION(GOOGLE)
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    if not grid:
        return count
    
    y_max = len(grid)
    x_max = len(grid[0])

    def helper(x,y):
        if 0<=x<x_max and 0<=y<y_max and grid[y][x]=="1":
            grid[y][x]="0"
            helper(x+1,y)
            helper(x-1,y)
            helper(x,y+1)
            helper(x,y-1)

    for y_idx in range(y_max):
        for x_idx in range(x_max):
            if grid[y_idx][x_idx]=="1":
                count+=1
                helper(x_idx,y_idx)
    return count

print(numIslands([["1","0","1","1","0","1","1"]]))
print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))