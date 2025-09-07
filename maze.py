from collections import deque


def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]  # Mark visited cells
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    came_from = {start: None}  # Parent map for path reconstruction
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right moves

    while queue:
        current = queue.popleft()

        if current == goal:
            # Reconstruct path by following parents back to start
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Reverse path to start->goal

        for d in directions:
            r, c = current[0] + d[0], current[1] + d[1]

            # Check boundaries and obstacles
            if 0 <= r < rows and 0 <= c < cols:
                if maze[r][c] != 'X' and not visited[r][c]:
                    queue.append((r, c))
                    visited[r][c] = True
                    came_from[(r, c)] = current

    return None  # No path found


# Define the maze grid
maze = [
    ['S', '.', '.', 'X', '.'],
    ['.', 'X', '.', 'X', '.'],
    ['.', 'X', '.', '.', '.'],
    ['.', '.', 'X', 'X', '.'],
    ['X', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (4, 4)

solution_path = bfs(maze, start, goal)

if solution_path:
    print("Shortest path found by BFS:")
    print(solution_path)
else:
    print("No path found.")
