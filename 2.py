from collections import deque

def shortest_path(matrix, start, end):
    # Проверяем корректность входных данных
    rows, cols = len(matrix), len(matrix[0])
    if not (0 <= start[0] < rows and 0 <= start[1] < cols):
        return -1  # Начальная точка вне границ
    if not (0 <= end[0] < rows and 0 <= end[1] < cols):
        return -1  # Конечная точка вне границ
    if matrix[start[0]][start[1]] == 0 or matrix[end[0]][end[1]] == 0:
        return -1  # Начальная или конечная точка недоступна

    # Направления движения (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Матрица для отслеживания посещенных клеток
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Инициализируем очередь для BFS
    queue = deque()
    queue.append((start[0], start[1], 0))  # (row, col, distance)
    visited[start[0]][start[1]] = True

    while queue:
        row, col, dist = queue.popleft()

        # Если достигли конечной точки, возвращаем расстояние
        if (row, col) == end:
            return dist

        # Проверяем всех соседей
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Проверяем, что соседняя клетка находится внутри матрицы
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if not visited[new_row][new_col] and matrix[new_row][new_col] == 1:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, dist + 1))

    # Если конечная точка недостижима
    return -1


# Пример использования
matrix = [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 1, 1, 1]
]

start = (0, 0)  # Начальная точка
end = (9, 9)    # Конечная точка

result = shortest_path(matrix, start, end)
if result != -1:
    print(f"Кратчайшее расстояние: {result}")
else:
    print("Путь невозможен")