import random
import math
import copy

# Génère une solution initiale aléatoire
def generer_random_solution(cities):
    solution = random.sample(cities, len(cities))
    print(f"liste initial {cities}")
    print(f"solution de base {solution}")
    return solution

# Calcule la distance totale d'un circuit
def calcul_distance(solution:list, cities:list, distance_matrix:list[list]):
    distance = 0
    for i in range(len(solution) - 1):
        x= cities.index(solution[i])
        y=cities.index(solution[i + 1])
        distance += distance_matrix[x][y]
    print(f"la longuer du chemin {solution} est {distance}")
    return distance

# Génère une solution voisine en échangeant deux villes
def generer_voisin(solution):
    neighbor = copy.deepcopy(solution[:])
    print(f"{neighbor}")
    a = random.randint(0, len(solution) - 1)
    b = random.randint(0, len(solution) - 1)
    while a==b:
        b = random.randint(0, len(solution) - 1)
    c=neighbor[a]
    d=neighbor[b]
    neighbor[a], neighbor[b] = d, c
    print(f"le vois est:{neighbor}")
    return neighbor

# Algorithme de recuit simulé
def recul_simule(cities, temperature, taux_refroidissement, matrice:list[list]):
    current_solution = generer_random_solution(cities)
    best_solution = current_solution
    
    while temperature>1:
        neighbor = generer_voisin(current_solution)
        delta = calcul_distance(neighbor,cities,matrice) - calcul_distance(current_solution,cities, matrice)
        if delta < 0:
            current_solution = neighbor
            if calcul_distance(current_solution,cities,matrice) < calcul_distance(best_solution,cities,matrice):
                best_solution = current_solution
        else:
            probability = math.exp(-delta / temperature)
            if random.random() < probability:
                current_solution = neighbor
        temperature *= taux_refroidissement
        
    return best_solution

# Exemple d'utilisation
cities = ["A", "B", "C", "D", "E","F"]
distance_matrix = [[0, 780, 320, 580, 480,660],
     [780, 0, 700, 460, 300,200],
     [320,700, 0, 380, 820,630],
     [580, 460, 380, 0,750,310],
     [480, 300, 820, 750,0,500],
     [660, 200, 630, 310,500,0]]

best_solution = recul_simule(cities, 100000, 0.95, distance_matrix)
print("\nBest solution:", best_solution)
print("Distance:", calcul_distance(best_solution,cities,distance_matrix))
