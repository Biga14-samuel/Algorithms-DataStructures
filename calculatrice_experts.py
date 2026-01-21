def calculer(a, b, operateur):
    """
    Exécute une opération arithmétique basée sur l'opérateur fourni.
    """
    match operateur:
        case "+":
            return a + b, "Addition"
        case "-":
            return a - b, "Soustraction"
        case "*":
            return a * b, "Multiplication"
        case "/":
            if b == 0: return "Erreur (Division par zéro)", "Division"
            return a / b, "Division"
        case "//":
            if b == 0: return "Erreur", "Division entière"
            return a // b, "Division entière (quotient)"
        case "%":
            return a % b, "Modulo (reste de la division)"
        case "**":
            return a ** b, "Puissance"
        case _:
            return None, "Inconnu"

def main():
    print("--- Super Calculatrice Python ---")
    try:
        n1 = float(input("Premier nombre : "))
        op = input("Opérateur (+, -, *, /, //, %, ** ) : ")
        n2 = float(input("Second nombre : "))

        resultat, nom_op = calculer(n1, n2, op)
        
        print(f"\nType d'opération : {nom_op}")
        print(f"Résultat : {n1} {op} {n2} = {resultat}")
        
    except ValueError:
        print("Erreur : Veuillez entrer des nombres valides.")

if __name__ == "__main__":
    main()