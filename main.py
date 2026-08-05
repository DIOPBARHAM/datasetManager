from menu import afficher_menu
from gestion import ajouter_dataset, afficher_datasets, rechercher_datasets, modifier_datasets, supprimer_datasets, trier_datasets
from statistiques import statistiques


# Menu
datasets = []

while True:

    afficher_menu()

    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_dataset()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "2":
        afficher_datasets()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "3":
        rechercher_datasets()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "4":
        modifier_datasets()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "5":
        supprimer_datasets()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "6":
        trier_datasets()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "7":
        statistiques()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "8":
        print("Fin du programme.")
        break

    else:
        print("Choix invalide.")
        input("Appuyez sur Entrée pour refaire un choix...")