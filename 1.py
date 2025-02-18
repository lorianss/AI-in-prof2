def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]  # Все 8 направлений

    def dfs(r, c):
        """Обход в глубину для отметки всех частей одного острова."""
        stack = [(r, c)]
        while stack:
            row, col = stack.pop()
            if 0 <= row < rows and 0 <= col < cols and not visited[row][col] and grid[row][col] == 1:
                visited[row][col] = True
                for dr, dc in directions:
                    stack.append((row + dr, col + dc))

    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                island_count += 1
                dfs(r, c)

    return island_count


# Пример использования
grid = [
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1]
]

result = count_islands(grid)
print("Количество островов:", result)