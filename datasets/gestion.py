import csv
import os
import sys

DOMAINES = (
    "Santé",
    "Finance",
    "Agriculture",
    "Transport",
    "Education"
)

datasets = []

def ajouter_dataset():

    print("\n=== Nouveau Dataset ===")

    nom = input("Nom : ")
# Gestion  des exceptions pour que le programme continue de fonctionner.
    while True:
        domaine = input("Domaine : ").title()

        if domaine in DOMAINES:
            break
        else:
            print("Domaine invalide.")
            print("Domaines autorisés :", DOMAINES)

    while True:

      try:
          lignes = int(input("Nombre de lignes : "))
          break
      
      except ValueError:
          print("Veuillez saisir un nombre entier.")



    while True:
    
          try:
              colonnes = int(input("Nombre de colonnes : "))
              break
          
          
          except ValueError:
              print("Veuillez saisir un nombre entier.")
    
    while True:
        
              try:
                  taille = float(input("Taille (Mo) : "))
                  break
              
              
              except ValueError:
                  print("Veuillez saisir un nombre .")

    while True:
        format_ds = input("Format (CSV/JSON) : ").upper()

        if format_ds in ("CSV", "JSON"):
            break
        print("Format invalide.")

    public = input("Public (true/false) : ").lower()

    if public not in ("true", "false"):
        print("Valeur invalide. Le dataset sera considéré comme privé.")
        print("Valeur autorisée : true ou false")
        public = input("Public (true/false) : ").lower()
    
    if public == "true":
        public = True
    else:
        public = False

    dataset = {
        "nom": nom,
        "domaine": domaine,
        "lignes": lignes,
        "colonnes": colonnes,
        "taille": taille,
        "format": format_ds,
        "public": public
    }

    datasets.append(dataset)

    print("\nDataset enregistré avec succès !")


def afficher_datasets():

    if len(datasets) == 0:
        print("\nAucun dataset enregistré.")
        return

    print("\n===== LISTE DES DATASETS =====")

    for i, ds in enumerate(datasets, start=1):

        print(f"\nDataset {i}")
        print("--------------------")

        for cle, valeur in ds.items():
            print(f"{cle} : {valeur}")

        

def rechercher_datasets():

    nom = input("Nom du dataset : ").lower()

    trouve = False
  # Gestion  des exceptions pour que le programme continue de fonctionner.
    for ds in datasets:

     if ds["nom"].lower() == nom.lower():

        print(ds)

    for ds in datasets:

        if ds["nom"].lower() == nom:
            print("\nDataset trouvé :")

            for cle, valeur in ds.items():
                print(f"{cle} : {valeur}")

            trouve = True

    if not trouve:
        print("Dataset introuvable.")





def modifier_datasets():

    nom = input("Nom du dataset à modifier : ").lower()

    for ds in datasets:

        if ds["nom"].lower() == nom:

            print("Nouvelles informations")

            ds["nom"] = input("Nom : ")
            ds["domaine"]=input("Domaine : ").title()
            ds["lignes"] = int(input("Nombre de lignes : "))
            ds["colonnes"] = int(input("Nombre de colonnes : "))
            ds["taille"] = float(input("Taille : "))
            ds["format"] = input("Format (CSV/JSON) : ").upper()
            ds["public"] = input("Public (true/false) : ").lower() == "true"

            print("Modification effectuée.")
            return

    print("Dataset introuvable.")



def supprimer_datasets():

    nom = input("Nom du dataset à supprimer : ").lower()

    for ds in datasets:

        if ds["nom"].lower() == nom:

            datasets.remove(ds)
            print("Dataset supprimé.")
            return

    print("Dataset introuvable.")



def trier_datasets():

    print("\n===== TRI DES DATASETS =====")
    if len(datasets) == 0:
        print("Aucun dataset.")
        return
   
    datasets.sort(key=lambda d: d["nom"].lower())
    print("Datasets triés par nom:")
    print("-" * 90)
    print(f"{'N°':<4} {'Nom':<15} {'Domaine':<15} {'Lignes':<10} {'Colonnes':<10} {'Taille':<10} {'Format':<8} {'Public'}")
    print("-" * 90)

    for i, ds in enumerate(datasets, start=1):

        print(f"{i:<4} "
              f"{ds['nom']:<15} "
              f"{ds['domaine']:<15} "
              f"{ds['lignes']:<10} "
              f"{ds['colonnes']:<10} "
              f"{ds['taille']:<10} "
              f"{ds['format']:<8} "
              f"{ds['public']}")

    print("-" * 90)



def sauvegarder():
    liste_datasets = datasets
    try:
        with open("datasets.csv", "w", newline="", encoding="utf-8") as fichier:
            champs = [
                "nom",
                "domaine",
                "lignes",
                "colonnes",
                "taille",
                "format",
                "public"
            ]

            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writeheader()

            for dataset in liste_datasets:
                writer.writerow(dataset)

        print("\nLes données ont été sauvegardées avec succès.")

    except Exception as e:
        print("Erreur lors de la sauvegarde :", e)




def recharger():
    liste_datasets = datasets
    try:
        with open("datasets.csv", "r", newline="", encoding="utf-8") as fichier:

            lecteur = csv.DictReader(fichier)

            liste_datasets.clear()

            for ligne in lecteur:

                dataset = {
                    "nom": ligne["nom"],
                    "domaine": ligne["domaine"],
                    "lignes": int(ligne["lignes"]),
                    "colonnes": int(ligne["colonnes"]),
                    "taille": float(ligne["taille"]),
                    "format": ligne["format"],
                    "public": ligne["public"] == "True"
                }

                liste_datasets.append(dataset)

        if len(liste_datasets) == 0:
            print("\nLe fichier est vide.")
        else:

            print("\n=== le fichier datasets.csv ===")

            champs = [
                    "nom",
                    "domaine",
                    "lignes",
                    "colonnes",
                    "taille",
                    "format",
                    "public"
                ]

            print(",".join(champs))

        for dataset in liste_datasets:
            ligne = [
                str(dataset["nom"]),
                str(dataset["domaine"]),
                str(dataset["lignes"]),
                str(dataset["colonnes"]),
                str(dataset["taille"]),
                str(dataset["format"]),
                str(dataset["public"])
            ]

            print(",".join(ligne))

    except FileNotFoundError:
        print("\nLe fichier datasets.csv n'existe pas.")

    except ValueError:
        print("\nErreur : données invalides dans le fichier.")

    except Exception as e:
        print("\nUne erreur est survenue :", e)