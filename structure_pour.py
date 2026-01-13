def calculer_carres(nombres):
    """
    Utilise une boucle 'pour' pour traiter chaque élément d'une liste.
    """
    resultats = []

    print(f"Liste d'origine : {nombres}")
    print("Début de l'itération...")

    # La structure POUR (FOR)
    # Pour chaque 'n' contenu dans la liste 'nombres'
    for n in nombres:
        carre = n * n
        resultats.append(carre)
        print(f"  Traitement de {n} : son carré est {carre}")

    return resultats

if __name__ == "__main__":
    ma_liste = [2, 4, 6, 8]
    liste_finale = calculer_carres(ma_liste)
    
    print(f"Traitement terminé. Nouvelle liste : {liste_finale}")