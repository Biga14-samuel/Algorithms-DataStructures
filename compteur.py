def compter_jusqua(limite):
    """
    Affiche les nombres de 1 jusqu'à la limite spécifiée.
    """
    print(f"Début du comptage jusqu'à {limite} :")
    
    # range(1, limite + 1) commence à 1 et s'arrête juste AVANT limite + 1
    for i in range(1, limite + 1):
        print(f"Nombre : {i}")
    
    print("Fin du comptage !")

if __name__ == "__main__":
    # On appelle la fonction pour compter jusqu'à 10
    compter_jusqua(10)