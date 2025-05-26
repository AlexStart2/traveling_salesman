import random
import time

# ---------------------------
# HILL CLIMBING IMPLEMENTATION
# ---------------------------

def generate_tour(n):
    tour = list(range(n))
    random.shuffle(tour)
    return tour

def calculate_tour_length(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i]][tour[(i + 1) % len(tour)]]
    return total_distance



def count_attacks(board):

    n = len(board)
    attacks = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(tour, distance_matrix):
    n = len(tour)
    best_tour = tour[:]
    best_distance = calculate_tour_length(tour, distance_matrix)

    for i in range(n):
        for j in range(i + 1, n):
            new_tour = tour[:]
            # Swap two cities
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_distance = calculate_tour_length(new_tour, distance_matrix)

            if new_distance < best_distance:
                best_tour = new_tour
                best_distance = new_distance

    return best_tour, best_distance


def hill_climbing_tsp(distance_matrix, max_restarts=10):
    n = len(distance_matrix)
    best_overall_tour = None
    best_overall_length = float('inf')
    start_time = time.time()

    for _ in range(max_restarts):
        tour = generate_tour(n)
        current_length = calculate_tour_length(tour, distance_matrix)

        while True:
            new_tour, new_length = get_best_neighbor(tour, distance_matrix)

            if new_length >= current_length:  # local optimum
                break

            tour = new_tour
            current_length = new_length

        if current_length < best_overall_length:
            best_overall_tour = tour
            best_overall_length = current_length

    execution_time = time.time() - start_time
    return best_overall_tour, best_overall_length, execution_time
