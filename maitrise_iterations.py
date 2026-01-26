def gerer_inventaire(articles):
    """
    Démontre les structures itératives et leur contrôle.
    """
    print(f"--- Analyse du stock ({len(articles)} articles) ---")

    for article in articles:
        # 1. Utilisation de 'continue' : on saute les articles vides
        if article == "":
            print("Article sans nom détecté, passage à l'élément suivant.")
            continue 
            
        # 2. Utilisation de 'break' : on arrête tout si on trouve un article dangereux
        if article == "Produit Toxique":
            print(f"ALERTE : {article} trouvé ! Arrêt immédiat de l'inventaire.")
            break
            
        print(f"Article validé : {article}")

if __name__ == "__main__":
    stock_magasin = ["Pomme", "", "Banane", "Produit Toxique", "Orange"]
    gerer_inventaire(stock_magasin)