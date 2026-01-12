def verifier_force_password(password):
    """
    Vérifie si un mot de passe est robuste.
    Critères : minimum 8 caractères et contient un caractère spécial.
    """
    # Liste de caractères spéciaux pour la vérification
    caracteres_speciaux = "!@#$%^&*"
    
    # Initialisation des scores
    longueur_ok = len(password) >= 8
    contient_special = any(char in caracteres_speciaux for char in password)
    
    if longueur_ok and contient_special:
        return "Fort 💪"
    elif longueur_ok or contient_special:
        return "Moyen ⚠️ (Il manque un critère)"
    else:
        return "Faible ❌ (Trop court et pas de caractères spéciaux)"

def main():
    print("--- Testeur de Robustesse de Mot de Passe ---")
    mdp = input("Entrez un mot de passe pour test : ")
    
    resultat = verifier_force_password(mdp)
    print(f"Force du mot de passe : {resultat}")

if __name__ == "__main__":
    main()