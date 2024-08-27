import random
import math

def rastrigin(x):
    return 20 + x[0]**2 + x[1]**2 - 10 * (math.cos(2 * math.pi * x[0]) + math.cos(2 * math.pi * x[1]))

def initialize_population(pop_size, bounds):
    population = []
    for _ in range(pop_size):
        individual = [random.uniform(bounds[0], bounds[1]), random.uniform(bounds[0], bounds[1])]
        population.append(individual)
    return population

def mutate_and_crossover(population, F, CR, bounds):
    new_population = []
    for i in range(len(population)):
        x = population[i]
        a, b, c = random.sample([ind for ind in population if ind != x], 3)
        
        y = []
        for j in range(len(x)):
            if random.random() < CR or j == random.randint(0, len(x) - 1):
                y_j = a[j] + F * (b[j] - c[j])
                # Ensure y_j is within bounds
                y_j = max(min(y_j, bounds[1]), bounds[0])
            else:
                y_j = x[j]
            y.append(y_j)
        
        # Selection
        if rastrigin(y) < rastrigin(x):
            new_population.append(y)
        else:
            new_population.append(x)
    
    return new_population

def differential_evolution(pop_size, bounds, F, CR, max_iterations):
    population = initialize_population(pop_size, bounds)
    best_individual = min(population, key=rastrigin)
    best_fitness = rastrigin(best_individual)
    
    for iteration in range(max_iterations):
        population = mutate_and_crossover(population, F, CR, bounds)
        current_best_individual = min(population, key=rastrigin)
        current_best_fitness = rastrigin(current_best_individual)
        
        # Update best solution found so far
        if current_best_fitness < best_fitness:
            best_individual = current_best_individual
            best_fitness = current_best_fitness
        
        # Display the best solution at each step
        print(f"Iteration {iteration + 1}: Best Solution = {best_individual}, Best Fitness = {best_fitness}")
    
    return best_individual, best_fitness

# Parameters
pop_size = 20 # simply 10*n, where n is dimension
bounds = [-5.12, 5.12]
F = 0.8
CR = 0.9
max_iterations = 1000

# Run the differential evolution algorithm
best_solution, best_fitness = differential_evolution(pop_size, bounds, F, CR, max_iterations)
print("Final Best Solution:", best_solution)
print("Final Best Fitness:", best_fitness)
