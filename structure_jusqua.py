def saisir_temperature():
    """
    Simule une structure 'Jusqu'à' : on demande une température
    jusqu'à ce que la valeur soit comprise entre -50 et 50.
    """
    print("--- Enregistrement de la Température ---")

    while True:  # On entre dans la boucle sans condition préalable
        try:
            temp = float(input("Entrez la température actuelle (entre -50 et 50) : "))
            
            # C'est ici que l'on définit la condition de sortie (le "Jusqu'à")
            if -50 <= temp <= 50:
                print(f"✅ Température de {temp}°C enregistrée avec succès.")
                break  # On sort de la boucle immédiatement
            else:
                print("❌ Valeur hors limites, recommencez.")
        
        except ValueError:
            print("❌ Erreur : Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    saisir_temperature()