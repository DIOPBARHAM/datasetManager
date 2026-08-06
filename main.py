from interface.menu import afficher_menu
from datasets.gestion import ajouter_dataset, afficher_datasets, recharger, rechercher_datasets, modifier_datasets, sauvegarder, supprimer_datasets, trier_datasets
from datasets.statistiques import statistiques


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
        sauvegarder()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "9":
        recharger()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "0":
        print("Fin du programme.")
        break

    else:
        print("Choix invalide.")
        input("Appuyez sur Entrée pour refaire un choix...")
