# Projet AAC – Résolution du Problème du Set Cover

## 1. Introduction

Le problème du **Set Cover** (problème de recouvrement d’ensembles) est un problème classique en algorithmique combinatoire. Il consiste à sélectionner un nombre minimal de sous-ensembles parmi une collection donnée afin de couvrir l’ensemble des éléments d’un univers.

Ce problème est connu pour être **NP-difficile**, ce qui signifie qu’il n’existe pas, à ce jour, d’algorithme polynomial permettant de trouver une solution optimale dans le cas général. Pour cette raison, des **algorithmes approchés**, notamment les algorithmes gloutons, sont couramment utilisés.

Ce projet s’inscrit dans le cadre du module **AAC (Algorithmique Avancée / Algorithmique Approchée)** et vise à comparer une approche gloutonne à une approche optimale par recherche exhaustive.

---

## 2. Objectifs du projet

Les objectifs principaux de ce travail sont les suivants :

- Modéliser le problème du Set Cover
- Implémenter un algorithme glouton pour obtenir une solution approchée
- Implémenter une recherche exhaustive afin de déterminer la solution optimale (pour des instances de petite taille)
- Comparer les deux solutions obtenues
- Évaluer la qualité de l’algorithme glouton à l’aide du **ratio d’approximation**

---

## 3. Définition du problème du Set Cover

Soit :
- Un univers fini \( U = \{1, 2, ..., n\} \)
- Une collection de sous-ensembles \( S = \{S_1, S_2, ..., S_m\} \) telle que \( S_i \subseteq U \)

Le problème du Set Cover consiste à trouver une sous-collection minimale \( C \subseteq S \) telle que :

\[
\bigcup_{S_i \in C} S_i = U
\]

---

## 4. Méthodologie adoptée

Deux approches ont été implémentées :

### 4.1 Approche gloutonne

L’algorithme glouton fonctionne de la manière suivante :

1. Initialiser l’ensemble des éléments non couverts
2. À chaque itération, sélectionner le sous-ensemble couvrant le plus grand nombre d’éléments encore non couverts
3. Ajouter ce sous-ensemble à la solution
4. Retirer les éléments couverts
5. Répéter jusqu’à couvrir tout l’univers

Cette approche ne garantit pas une solution optimale, mais fournit une **solution approchée efficace en temps polynomial**.

---

### 4.2 Approche optimale (recherche exhaustive)

Pour des instances de petite taille, une recherche exhaustive est utilisée :

- Toutes les combinaisons possibles de sous-ensembles sont testées
- La première combinaison couvrant l’univers avec le nombre minimal de sous-ensembles est retenue

Cette approche garantit l’optimalité de la solution, mais présente une **complexité exponentielle**, ce qui limite son usage à des cas de petite taille.

---

## 5. Description des fonctions implémentées

### `generate_instance(n, m, min_size, max_size)`
Génère une instance aléatoire du problème du Set Cover :
- `n` : taille de l’univers
- `m` : nombre de sous-ensembles
- `min_size`, `max_size` : tailles minimales et maximales des sous-ensembles

---

### `set_cover_glouton(U, subsets)`
Implémente l’algorithme glouton du Set Cover :
- Sélectionne itérativement le sous-ensemble le plus couvrant
- Retourne une solution approchée

---

### `set_cover_optimal(U, subsets)`
Implémente une recherche exhaustive :
- Teste toutes les combinaisons possibles
- Retourne la solution optimale si elle existe

---

### `main()`
- Génère une instance du problème
- Applique les deux algorithmes
- Affiche les résultats obtenus
- Calcule le ratio d’approximation

---

## 6. Exécution du programme

### 6.1 Prérequis
- Python 3.x
- Bibliothèques standards uniquement (`random`, `itertools`)

### 6.2 Lancement
```bash
python Projet_AAC.py
