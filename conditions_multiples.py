def calculer_prix_ticket(age):
    """
    Détermine le prix du billet selon plusieurs conditions d'âge.
    Structure : if / elif / elif / else
    """
    if age < 4:
        # Condition 1
        prix = 0
        categorie = "Bébé (Gratuit)"
    elif age < 12:
        # Condition 2 (si la condition 1 est fausse)
        prix = 5
        categorie = "Enfant"
    elif age < 18:
        # Condition 3 (si les conditions 1 et 2 sont fausses)
        prix = 8
        categorie = "Adolescent"
    elif age >= 65:
        # Condition 4
        prix = 7
        categorie = "Sénior"
    else:
        # Cas par défaut (si aucune des conditions ci-dessus n'est vraie)
        prix = 12
        categorie = "Adulte"
    
    return categorie, prix

if __name__ == "__main__":
    try:
        age_utilisateur = int(input("Veuillez entrer votre âge : "))
        cat, tarif = calculer_prix_ticket(age_utilisateur)
        
        print(f"--- Résultat ---")
        print(f"Catégorie : {cat}")
        print(f"Tarif à payer : {tarif}€")
        
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier pour l'âge.")