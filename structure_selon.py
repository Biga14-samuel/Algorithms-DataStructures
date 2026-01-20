def menu_cafe(choix):
    """
    Simule une structure 'Selon' (Match/Case) pour traiter une commande.
    """
    match choix.lower():
        case "espresso":
            return "Un café fort et court. Arrive tout de suite !"
        case "latte":
            return "Un café doux avec beaucoup de lait mousseux."
        case "cappuccino":
            return "Un équilibre parfait entre café et mousse."
        case "thé":
            return "De l'eau chaude et des feuilles de thé infusées."
        case _:  # Le cas par défaut (équivalent du 'else' ou 'default')
            return "❓ Désolé, nous ne servons pas cette boisson."

if __name__ == "__main__":
    print("--- Bienvenue au Python Café ---")
    commande = input("Que souhaitez-vous commander ? (Espresso, Latte, Cappuccino, Thé) : ")
    
    resultat = menu_cafe(commande)
    print(resultat)