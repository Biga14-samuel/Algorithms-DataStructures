def demo_tableaux():
    print("--- Déclaration et Initialisation des Tableaux (Listes) ---")

    # 1. Déclaration et initialisation d'une liste vide
    panier = []
    print(f"1. Liste vide créée : {panier}")

    # 2. Initialisation avec des valeurs (Strings)
    fruits = ["Pomme", "Banane", "Cerise"]
    print(f"2. Liste de fruits : {fruits}")

    # 3. Accès aux éléments (L'index commence à 0)
    premier_fruit = fruits[0]
    print(f"3. Le premier fruit est : {premier_fruit}")

    # 4. Modification d'un élément
    fruits[1] = "Mangue"
    print(f"4. Après modification du 2ème élément : {fruits}")

    # 5. Ajout dynamique (Initialisation progressive)
    fruits.append("Orange")
    print(f"5. Après ajout d'un fruit : {fruits}")

    # 6. Suppression d'un élément
    fruits.remove("Cerise")
    print(f"6. Après suppression de 'Cerise' : {fruits}")

    # 7. Taille du tableau
    taille = len(fruits)
    print(f"7. Le tableau contient maintenant {taille} éléments.")

if __name__ == "__main__":
    demo_tableaux()