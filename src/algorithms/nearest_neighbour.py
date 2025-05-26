import time
import random

def tsp_nearest_neighbour(distance_matrix, stop_type='time', stop_value=60):
    n = len(distance_matrix)
    best_cost = float('inf')
    best_path = []
    solutions_found = 0
    start_time = time.time()

    def time_exceeded():
        return stop_type == 'time' and (time.time() - start_time) >= stop_value

    while True:
        if stop_type == 'count' and solutions_found >= stop_value:
            break
        if time_exceeded():
            break

        start_city = random.randint(0, n - 1)
        unvisited = set(range(n))
        path = [start_city]
        unvisited.remove(start_city)

        while unvisited:
            last = path[-1]
            next_city = min(unvisited, key=lambda city: distance_matrix[last][city])
            path.append(next_city)
            unvisited.remove(next_city)

        # injectam zgomot

        # iteration = 0
        # while unvisited:
        #     last = path[-1]
        #     distances = [(city, distance_matrix[last][city]) for city in unvisited]
        #     distances.sort(key=lambda x: x[1])

        #     if iteration == 2 and len(distances) > 1:
        #         # Alege a doua cea mai apropiata
        #         next_city = distances[1][0]
        #     else:
        #         # Alege cea mai apropiata
        #         next_city = distances[0][0]

        #     path.append(next_city)
        #     unvisited.remove(next_city)
        #     iteration += 1

        path.append(start_city)  # return to starting city
        cost = sum(distance_matrix[path[i]][path[i + 1]] for i in range(n))

        solutions_found += 1
        if cost < best_cost:
            best_cost = cost
            best_path = path

    exec_time = time.time() - start_time
    return exec_time, solutions_found, (best_cost, best_path)