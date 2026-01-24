def systeme_connexion(utilisateur_saisi, mdp_saisi):
    """
    Démontre les structures conditionnelles imbriquées.
    """
    # Base de données fictive
    USER_VALIDE = "admin"
    MDP_VALIDE = "12345"

    print(f"Tentative de connexion pour : {utilisateur_saisi}")

    # Structure conditionnelle de niveau 1 : Vérification de l'identifiant
    if utilisateur_saisi == USER_VALIDE:
        print("Utilisateur reconnu.")
        
        # Structure conditionnelle de niveau 2 : Vérification du mot de passe
        if mdp_saisi == MDP_VALIDE:
            return "Accès accordé. Bienvenue dans votre tableau de bord."
        else:
            return "Mot de passe incorrect. Échec de la connexion."
            
    else:
        # Si le niveau 1 échoue
        return "Utilisateur inconnu. Veuillez créer un compte."

if __name__ == "__main__":
    user = input("Identifiant : ")
    password = input("Mot de passe : ")
    
    resultat = systeme_connexion(user, password)
    print(f"Résultat du système : {resultat}")