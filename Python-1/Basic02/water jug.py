from collections import deque

def water_jug_problem(capacity_a, capacity_b, target_a, target_b):
    """
    Solves the Water Jug Problem using Breadth-First Search (BFS).

    ... (rest of the docstring remains the same)
    """
    if target_a > capacity_a or target_b > capacity_b:
        return None  # Target cannot be reached if it exceeds capacities

    # Initialize the queue for BFS with the initial state (both jugs empty)
    queue = deque([(0, 0, [])])  # (water_a, water_b, path)
    visited = set()  # To avoid revisiting states

    while queue:
        water_a, water_b, path = queue.popleft()

        # Check if the target state is reached
        if water_a == target_a and water_b == target_b:
            return path + [(water_a, water_b)]  # Return the solution path

        # Mark the current state as visited
        visited.add((water_a, water_b))

        # Define all possible operations as a list of functions
        operations = [
            (capacity_a, water_b, path + [(water_a, water_b)]),  # Fill A
            (water_a, capacity_b, path + [(water_a, water_b)]),  # Fill B
            (0, water_b, path + [(water_a, water_b)]),          # Empty A
            (water_a, 0, path + [(water_a, water_b)]),          # Empty B
            (max(0, water_a - (capacity_b - water_b)), min(capacity_b, water_b + water_a), path + [(water_a, water_b)]), # Pour A to B
            (min(capacity_a, water_a + water_b), max(0, water_b - (capacity_a - water_a)), path + [(water_a, water_b)]), # Pour B to A
        ]

        # Explore the next states by applying each operation
        for next_a, next_b, next_path in operations:
            if (next_a, next_b) not in visited:
                queue.append((next_a, next_b, next_path))

    return None  # No solution found

def print_solution(solution):
    """
    Prints the solution path in a user-friendly format.

    ... (rest of the docstring remains the same)
    """
    if solution is None:
        print("No solution found.")
    else:
        print("Solution:")
        for i, (a, b) in enumerate(solution):
            print(f"Step {i}: Jug A = {a}, Jug B = {b}")

if __name__ == "__main__":
    # Example usage:
    capacity_a = 4
    capacity_b = 3
    target_a = 2
    target_b = 0

    solution = water_jug_problem(capacity_a, capacity_b, target_a, target_b)
    print_solution(solution)

    # Example with no solution
    capacity_a = 5
    capacity_b = 2
    target_a = 3
    target_b = 4
    solution = water_jug_problem(capacity_a, capacity_b, target_a, target_b)
    print_solution(solution)