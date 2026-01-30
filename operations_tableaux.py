def demo_operations_courantes():
    # Initialisation d'une liste de scores désordonnée
    scores = [45, 12, 89, 33, 45, 67]
    print(f"Scores originaux : {scores}")

    # 1. Trier la liste (Ordre croissant)
    scores.sort()
    print(f"1. Scores triés : {scores}")

    # 2. Inverser l'ordre (Du plus grand au plus petit)
    scores.reverse()
    print(f"2. Ordre décroissant : {scores}")

    # 3. Compter le nombre d'occurrences
    # Combien de fois le score 45 apparaît ?
    nombre_de_45 = scores.count(45)
    print(f"3. Le score 45 apparaît {nombre_de_45} fois.")

    # 4. Trouver la valeur maximale et minimale
    # Très utile pour les statistiques
    print(f"4. Meilleur score : {max(scores)} | Moins bon score : {min(scores)}")

    # 5. Calculer la somme (pour faire une moyenne par exemple)
    total = sum(scores)
    moyenne = total / len(scores)
    print(f"5. Somme totale : {total} | Moyenne : {moyenne:.2f}")

    # 6. Vider la liste
    scores.clear()
    print(f"6. Liste après nettoyage : {scores}")

if __name__ == "__main__":
    demo_operations_courantes()