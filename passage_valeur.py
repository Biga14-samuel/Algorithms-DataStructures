def tentative_modification(nombre):
    """
    Démontre le passage par valeur (types immuables).
    """
    print(f"À l'intérieur de la fonction (avant) : {nombre}")
    
    # On modifie la variable locale
    nombre = nombre + 10
    
    print(f"À l'intérieur de la fonction (après modification) : {nombre}")

if __name__ == "__main__":
    # Variable originale
    score_original = 50
    
    print(f"Avant l'appel de la fonction, le score est : {score_original}")
    
    # On passe 'score_original' à la fonction
    tentative_modification(score_original)
    
    print(f"Après l'appel, le score original est TOUJOURS : {score_original}")
    print("\nNote : La variable originale n'a pas été modifiée car c'est une copie qui a été manipulée.")