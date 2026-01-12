from collections import deque

def solve_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = {tuple(start)}
    
    while queue:
        state, path = queue.popleft()
        if state == goal: return path + [state]
        
        idx = state.index(0)
        # Calculate possible moves (row/col shifts)
        for move in (-3, 3, -1, 1): 
            new_idx = idx + move
            # Boundary checks: stay in grid and prevent wrap-around moves
            if 0 <= new_idx < 9 and not (idx % 3 == 0 and move == -1) and not (idx % 3 == 2 and move == 1):
                new_state = list(state)
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                if tuple(new_state) not in visited:
                    visited.add(tuple(new_state))
                    queue.append((new_state, path + [state]))

# Execution
start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
result = solve_puzzle(start, goal)

for i, step in enumerate(result):
    print(f"Step {i}: {step[:3]}\n        {step[3:6]}\n        {step[6:]}\n")