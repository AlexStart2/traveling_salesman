import time
import itertools

# ---------------------------
# BACKTRACKING IMPLEMENTATION
# ---------------------------

def tsp_backtracking(distance_matrix, stop_type='time', stop_value=60):
    n = len(distance_matrix)
    best_cost = float('inf')
    best_path = []
    solutions_found = 0
    start_time = time.time()

    cities = list(range(n))

    def time_exceeded():
        return stop_type == 'time' and (time.time() - start_time) >= stop_value

    for perm in itertools.permutations(cities[1:]):  # fix the start at city 0
        if stop_type == 'count' and solutions_found >= stop_value:
            break
        if time_exceeded():
            break

        path = [0] + list(perm) + [0]
        cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(n))
        solutions_found += 1

        if cost < best_cost:
            best_cost = cost
            best_path = path

    exec_time = time.time() - start_time
    return exec_time, solutions_found, (best_cost, best_path)