def verifier_eligibilite(age, a_un_emploi, epargne):
    """
    Utilise les opérateurs logiques : and, or, not.
    """
    print(f"--- Analyse des critères : Age={age}, Emploi={a_un_emploi}, Épargne={epargne}€ ---")

    # 1. L'opérateur AND (ET) : Toutes les conditions doivent être vraies
    # Condition : Avoir entre 18 et 65 ans ET avoir un emploi
    eligible_pret = (age >= 18 and age <= 65) and a_un_emploi
    
    # 2. L'opérateur OR (OU) : Au moins une des conditions doit être vraie
    # Condition : Être éligible au prêt OU avoir plus de 10 000€ d'épargne
    acces_prioritaire = eligible_pret or epargne > 10000
    
    # 3. L'opérateur NOT (NON) : Inverse le résultat
    # Condition : Vérifier si la personne n'est PAS mineure
    est_majeur = not (age < 18)

    print(f"Est majeur ? {est_majeur}")
    print(f"Éligible au prêt standard ? {eligible_pret}")
    print(f"Accès au salon prioritaire ? {acces_prioritaire}")

    if eligible_pret:
        return "Félicitations, votre dossier est solide !"
    elif acces_prioritaire:
        return "Dossier accepté grâce à votre épargne."
    else:
        return "Dossier refusé : les critères ne sont pas remplis."

if __name__ == "__main__":
    # Testons avec des données
    mon_age = 25
    travail = True
    mon_epargne = 5000
    
    resultat = verifier_eligibilite(mon_age, travail, mon_epargne)
    print(f"\nConclusion : {resultat}")