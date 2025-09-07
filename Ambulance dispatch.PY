import heapq

def heuristic(a, b):
    # Manhattan distance as heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(start, goal, city_map):
    # city_map is a 2D grid: 0 = road, 1 = obstacle
    rows, cols = len(city_map), len(city_map[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        est_total_cost, cost_so_far, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, cost_so_far
        if current in visited:
            continue
        visited.add(current)

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and city_map[nx][ny] == 0:
                if (nx, ny) not in visited:
                    new_cost = cost_so_far + 1  # assuming uniform cost
                    est_cost = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_set, (est_cost, new_cost, (nx, ny), path + [(nx, ny)]))
    return None, float('inf')

# Example usage
city_map = [
    [0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
]
ambulance_start = (0, 0)
emergency_location = (3, 4)

path, cost = astar_search(ambulance_start, emergency_location, city_map)
print("Dispath path:", path)
print("Path cost (time):", cost)
