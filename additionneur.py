def additionner_entiers(nombre1, nombre2):
    """
    Calcule la somme de deux nombres.
    """
    return nombre1 + nombre2

def executer_programme():
    print("--- Calculateur d'Addition ---")
    
    try:
        # On convertit l'entrée en entier (int)
        num1 = int(input("Entrez le premier nombre entier : "))
        num2 = int(input("Entrez le second nombre entier : "))
        
        resultat = additionner_entiers(num1, num2)
        
        print(f"Le résultat de {num1} + {num2} est : {resultat}")
        
    except ValueError:
        # Gestion d'erreur si l'utilisateur ne tape pas un chiffre
        print("Erreur : Veuillez entrer des nombres entiers valides.")

if __name__ == "__main__":
    executer_programme()