def demo_acces_expert():
    # Initialisation d'un tableau de données
    # Imaginez une file d'attente de clients
    clients = ["Alice", "Bob", "Charlie", "David", "Eve"]
    
    print(f"File complète : {clients}")

    # 1. Accès direct (Indexation positive)
    # L'ordinateur va directement à l'adresse mémoire
    print(f"Premier client (index 0) : {clients[0]}")
    print(f"Troisième client (index 2) : {clients[2]}")

    # 2. Accès par la fin (Indexation négative)
    # Très utile quand on ne connaît pas la taille de la liste
    print(f"Dernier client (index -1) : {clients[-1]}")
    print(f"Avant-dernier client (index -2) : {clients[-2]}")

    # 3. Le Découpage (Slicing) - Accès à une sous-partie
    # Format : [début : fin_exclue]
    print(f"Les deux premiers (0 à 2) : {clients[0:2]}")
    print(f"Du deuxième à la fin : {clients[1:]}")
    
    # 4. Accès par recherche (Trouver l'index)
    index_bob = clients.index("Bob")
    print(f"Bob se trouve à la position : {index_bob}")

if __name__ == "__main__":
    demo_acces_expert()