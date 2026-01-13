from collections import deque

def water_jug_solver(jug1_cap, jug2_cap, target):
    # Queue stores (amt_jug1, amt_jug2, steps_taken)
    queue = deque([(0, 0, [])])
    visited = set([(0, 0)])

    while queue:
        j1, j2, steps = queue.popleft()

        # Check if we reached the target in either jug
        if j1 == target or j2 == target:
            return steps + [f"Goal reached: ({j1}, {j2})"]

        # Define all possible moves
        moves = [
            (jug1_cap, j2, "Fill Jug 1"),          # Fill Jug 1
            (j1, jug2_cap, "Fill Jug 2"),          # Fill Jug 2
            (0, j2, "Empty Jug 1"),                # Empty Jug 1
            (j1, 0, "Empty Jug 2"),                # Empty Jug 2
            (j1 - min(j1, jug2_cap - j2), j2 + min(j1, jug2_cap - j2), "Pour 1 -> 2"), # Pour 1 to 2
            (j1 + min(j2, jug1_cap - j1), j2 - min(j2, jug1_cap - j1), "Pour 2 -> 1")  # Pour 2 to 1
        ]

        for next_j1, next_j2, move_desc in moves:
            if (next_j1, next_j2) not in visited:
                visited.add((next_j1, next_j2))
                queue.append((next_j1, next_j2, steps + [f"{move_desc} -> ({next_j1}, {next_j2})"]))

    return "No solution possible."

# Example: Jug1=4L, Jug2=3L, Target=2L
solution = water_jug_solver(4, 3, 2)
for step in solution:
    print(step)