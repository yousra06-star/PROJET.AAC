
import random
from itertools import combinations



def generate_instance(n, m, min_size=2, max_size=5):
    """
    Génère une instance du problème Set Cover
    n : taille de l'univers
    m : nombre de sous-ensembles
    """
    U = set(range(1, n + 1))
    subsets = []

    for _ in range(m):
        size = random.randint(min_size, max_size)
        subset = set(random.sample(list(U), min(size, n)))
        subsets.append(subset)

    return U, subsets



def set_cover_glouton(U, subsets):
    """
    Algorithme glouton du Set Cover
    Retourne une solution approchée
    """
    U_rest = set(U)
    solution = []

    while U_rest:
        
        best_subset = max(subsets, key=lambda s: len(s & U_rest))

        
        if len(best_subset & U_rest) == 0:
            break

        solution.append(best_subset)
        U_rest -= best_subset

    return solution



def set_cover_optimal(U, subsets):
    """
    Recherche exhaustive de la solution optimale
    Réservée aux petites instances
    """
    m = len(subsets)

    for r in range(1, m + 1):
        for comb in combinations(subsets, r):
            if set().union(*comb) == U:
                return list(comb)

    return None



def main():
    
    n = 10   
    m = 8    

    U, subsets = generate_instance(n, m)

    print("===================================")
    print("Univers U :", U)
    print("Sous-ensembles :")
    for i, s in enumerate(subsets):
        print(f"S{i+1} =", s)

    
    sol_glouton = set_cover_glouton(U, subsets)
    sol_optimal = set_cover_optimal(U, subsets)

    print("\n===================================")
    print("Résultats")
    print("-----------------------------------")
    print("Solution gloutonne :")
    for s in sol_glouton:
        print(s)
    print("Taille gloutonne :", len(sol_glouton))

    if sol_optimal is not None:
        print("\nSolution optimale :")
        for s in sol_optimal:
            print(s)
        print("Taille optimale :", len(sol_optimal))
        print("Ratio d'approximation :", len(sol_glouton) / len(sol_optimal))
    else:
        print("\nSolution optimale non calculée (instance trop grande)")

    print("===================================")



if __name__ == "__main__":
    main()
