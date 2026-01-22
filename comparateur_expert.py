def analyser_valeur(valeur, seuil_critique):
    """
    Utilise tous les opérateurs de comparaison pour situer une valeur par rapport à un seuil.
    """
    print(f"--- Analyse de la valeur {valeur} par rapport au seuil {seuil_critique} ---")

    # Utilisation des 6 opérateurs de comparaison
    print(f"1. Égalité (==) : {valeur == seuil_critique}")
    print(f"2. Différence (!=) : {valeur != seuil_critique}")
    print(f"3. Strictement supérieur (>) : {valeur > seuil_critique}")
    print(f"4. Strictement inférieur (<) : {valeur < seuil_critique}")
    print(f"5. Supérieur ou égal (>=) : {valeur >= seuil_critique}")
    print(f"6. Inférieur ou égal (<=) : {valeur <= seuil_critique}")

    # Exemple concret d'utilisation
    if valeur > seuil_critique:
        return "Alerte : Seuil dépassé !"
    elif valeur == seuil_critique:
        return "Attention : Valeur exactement égale au seuil."
    else:
        return "Tout est normal."

if __name__ == "__main__":
    try:
        score = float(input("Entrez une valeur a tester : "))
        seuil = 100.0
        
        message = analyser_valeur(score, seuil)
        print(f"\nConclusion : {message}")
        
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")