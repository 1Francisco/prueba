from collections import deque
import copy

def solve_maze(maze):
    n_rows, n_cols = len(maze), len(maze[0])
    start = (0, 0)
    end = (n_rows - 1, n_cols - 1)

    # Verificación inicial
    if maze[0][0] == 0 or maze[end[0]][end[1]] == 0:
        return None

    # Movimiento en 4 direcciones
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS setup
    queue = deque([start])
    visited = set()
    visited.add(start)

    # Para reconstruir el camino
    parent = {}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for d in directions:
            nr, nc = current[0] + d[0], current[1] + d[1]
            next_cell = (nr, nc)
            if 0 <= nr < n_rows and 0 <= nc < n_cols and maze[nr][nc] == 1 and next_cell not in visited:
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    # No se encontró camino
    if end not in parent:
        return None

    # Reconstruir el camino
    path = set()
    cell = end
    while cell != start:
        path.add(cell)
        cell = parent[cell]
    path.add(start)

    # Construir matriz de salida
    result = []
    for i in range(n_rows):
        row = []
        for j in range(n_cols):
            row.append('S' if (i, j) in path else '-')
        result.append(row)
    return result

def print_maze(maze):
    for row in maze:
        print(row)
    print()

if __name__ == '__main__':
    test_mazes = {
        "m": [[1, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 0, 0, 1],
              [1, 1, 1, 1]],

        "easy_maze": [
            [1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 1]
        ],

        "medium_maze": [
            [1, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1]
        ],

        "hard_maze": [
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]
        ]
    }

    for name, maze in test_mazes.items():
        print(f"Solving {name}...")
        solution = solve_maze(maze)
        if solution:
            print_maze(solution)
        else:
            print("No path found.\n")
