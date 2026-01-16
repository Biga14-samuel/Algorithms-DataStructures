def systeme_alarme():
    """
    Simule une saisie de code de sécurité. 
    La boucle continue tant que le code est faux.
    """
    code_secret = "1234"
    code_saisi = ""
    tentatives = 0

    print("--- Système de Sécurité ---")

    # La structure TANT QUE (WHILE)
    # On continue tant que le code est différent du code secret
    while code_saisi != code_secret:
        code_saisi = input("Entrez le code secret pour désactiver l'alarme : ")
        tentatives += 1
        
        if code_saisi != code_secret:
            print(f"❌ Code incorrect. (Tentative n°{tentatives})")

    print(f"✅ Code correct ! Alarme désactivée après {tentatives} tentative(s).")

if __name__ == "__main__":
    systeme_alarme()