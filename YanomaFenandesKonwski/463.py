def islandPerimeter(grid):
    if not grid:
        return 0
    resposta = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                resposta += 4
                if i > 0 and grid[i-1][j] == 1:  
                    resposta -= 2
                if j > 0 and grid[i][j-1] == 1:  
                    resposta -= 2
    return resposta

grade = [[1,0]]
print(islandPerimeter(grade))  