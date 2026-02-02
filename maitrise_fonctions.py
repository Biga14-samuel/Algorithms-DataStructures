def calculer_tva(prix_ht, taux=20):
    """
    Fonction qui calcule le montant de la TVA.
    Retourne la valeur calculée.
    """
    montant_tva = (prix_ht * taux) / 100
    return montant_tva

def calculer_prix_ttc(prix_ht, taux_tva=20):
    """
    Fonction qui utilise une autre fonction pour calculer le prix final.
    """
    tva = calculer_tva(prix_ht, taux_tva)
    return prix_ht + tva

def formater_monnaie(valeur):
    """Transforme un nombre en une chaîne lisible."""
    return f"{valeur:.2f} €"

if __name__ == "__main__":
    prix_article = 150.0
    
    # On récupère les résultats des fonctions dans des variables
    tva_a_payer = calculer_tva(prix_article)
    total_final = calculer_prix_ttc(prix_article)

    print(f"Prix HT : {formater_monnaie(prix_article)}")
    print(f"TVA (20%) : {formater_monnaie(tva_a_payer)}")
    print(f"Total à payer : {formater_monnaie(total_final)}")