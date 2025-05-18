import heapq

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Directions: (row_offset, col_offset)
moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

def manhattan_distance(state):
    distance = 0
    for i, value in enumerate(state):
        if value == 0:
            continue
        goal_pos = goal_state.index(value)
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_pos, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    for move, offset in moves.items():
        new_index = zero_index + offset
        if move == 'up' and row == 0: continue
        if move == 'down' and row == 2: continue
        if move == 'left' and col == 0: continue
        if move == 'right' and col == 2: continue

        new_state = list(state)
        new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
        neighbors.append(tuple(new_state))

    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star(start):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start), 0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, cost, current = heapq.heappop(open_set)

        if current == goal_state:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def main():
    print("Enter the 8-puzzle start state (use 0 for the blank):")
    try:
        tiles = list(map(int, input("Enter 9 space-separated numbers: ").strip().split()))
        if len(tiles) != 9 or set(tiles) != set(range(9)):
            print("Error: Please enter numbers from 0 to 8 exactly once.")
            return
    except:
        print("Invalid input.")
        return

    start_state = tuple(tiles)
    solution = a_star(start_state)

    if solution:
        print("\nSolved in", len(solution) - 1, "moves.")
        for step in solution:
            print_puzzle(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

"""

1 2 3 4 5 6 0 7 8 → 2 moves

1 2 3 4 0 6 7 5 8 → 4 moves

1 2 3 0 5 6 4 7 8 → 4 moves

1 2 3 5 0 6 4 7 8 → 6 moves

1 3 6 5 0 2 4 7 8 → 8 moves
"""