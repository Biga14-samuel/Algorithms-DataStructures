def afficher_separateur():
    """Procédure simple : affiche une ligne décorative."""
    print("-" * 40)

def afficher_entete(titre):
    """Procédure avec paramètre : formate un titre en majuscules."""
    afficher_separateur()
    print(f"SÉCTION : {titre.upper()}")
    afficher_separateur()

def analyser_donnees(nom_projet, status_ok):
    """Procédure logique : effectue une action selon une condition."""
    afficher_entete(nom_projet)
    if status_ok:
        print("Statut : Opérationnel")
    else:
        print("Statut : Erreur système détectée")
    afficher_separateur()
    print("\n") # Saut de ligne pour la lisibilité

if __name__ == "__main__":
    # Appel des procédures
    analyser_donnees("Base de données", True)
    analyser_donnees("Serveur Web", False)
    analyser_donnees("Système de Paiement", True)