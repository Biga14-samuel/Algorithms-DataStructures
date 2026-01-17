def determiner_mention(note):
    """
    Détermine la mention en fonction de la note (sur 20).
    Structure : Si ... Alors ... Sinon Si ... Sinon
    """
    print(f"Analyse de la note : {note}/20")

    if note >= 16:
        # SI la note est >= 16
        return "Très Bien"
    elif note >= 14:
        # SINON SI la note est >= 14
        return "Bien"
    elif note >= 12:
        # SINON SI la note est >= 12
        return "Assez Bien"
    elif note >= 10:
        # SINON SI la note est >= 10
        return "Passable"
    else:
        # SINON (si aucune des conditions précédentes n'est vraie)
        return "Insuffisant"

if __name__ == "__main__":
    try:
        ma_note = float(input("Entrez votre note (0-20) : "))
        
        if 0 <= ma_note <= 20:
            resultat = determiner_mention(ma_note)
            print(f"Résultat : {resultat}")
        else:
            print("Erreur : La note doit être comprise entre 0 et 20.")
            
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")