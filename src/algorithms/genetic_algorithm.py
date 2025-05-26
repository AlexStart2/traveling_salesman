import random
import time

def genetic_tsp(distance_matrix,
                population_size=100,
                generations=100,
                mutation_rate=0.02,
                tournament_size=5):
    """
    Algoritm Genetic pentru TSP.
    distance_matrix: list of lists, matrice simetrica de distante
    population_size: marimea populatiei
    generations: cate generatii rulam
    mutation_rate: probabilitatea de mutatie pe individ
    tournament_size: marimea turneului pentru selectie
    """
    n = len(distance_matrix)
    
    def tour_length(tour):
        return sum(distance_matrix[tour[i]][tour[(i+1)%n]] for i in range(n))
    
    def random_tour():
        t = list(range(n))
        random.shuffle(t)
        return t

    def crossover(parent1, parent2):
        # Ordered Crossover (OX)
        a, b = sorted(random.sample(range(n), 2))
        child = [-1]*n
        # pastreaza sectiunea [a:b] din p1
        child[a:b] = parent1[a:b]
        # umple restul in ordinea din p2
        pos = b
        for city in parent2[b:] + parent2[:b]:
            if city not in child:
                if pos >= n: pos = 0
                child[pos] = city
                pos += 1
        return child

    def mutate(tour):
        # Swap mutation
        i, j = random.sample(range(n), 2)
        tour[i], tour[j] = tour[j], tour[i]

    def tournament_select(pop):
        # alege cel mai bun dintre k indivizi random
        competitors = random.sample(pop, tournament_size)
        return min(competitors, key=lambda t: tour_length(t))

    # Initializeaza populatia
    population = [random_tour() for _ in range(population_size)]
    best_tour = min(population, key=tour_length)
    best_cost = tour_length(best_tour)

    start_time = time.time()
    for gen in range(generations):
        new_pop = []
        # elitism: pastreaza cel mai bun
        new_pop.append(best_tour[:])

        # restul populatiei
        while len(new_pop) < population_size:
            # selectie
            p1 = tournament_select(population)
            p2 = tournament_select(population)
            # incrucisare
            child = crossover(p1, p2)
            # mutatie
            if random.random() < mutation_rate:
                mutate(child)
            new_pop.append(child)

        population = new_pop
        # actualizeaza best
        current_best = min(population, key=tour_length)
        current_cost = tour_length(current_best)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_best[:]

    exec_time = time.time() - start_time
    return exec_time, best_cost, best_tour
