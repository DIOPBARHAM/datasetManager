import csv
import os


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


def afficher():

    if len(datasets) == 0:
        print("\nAucun dataset enregistré.")
        return

    print("\n===== LISTE DES DATASETS =====")

    for i, ds in enumerate(datasets, start=1):

        print(f"\nDataset {i}")
        print("--------------------")

        for cle, valeur in ds.items():
            print(f"{cle} : {valeur}")
            



def rechercher():

    nom = input("Nom du dataset : ").lower()

    trouve = False
  # Gestion  des exceptions pour que le programme continue de fonctionner.
    for ds in datasets:

     if ds["nom"].lower() == nom.lower():

        print(ds)
        return

     raise LookupError("Dataset introuvable.")

    for ds in datasets:

        if ds["nom"].lower() == nom:
            print("\nDataset trouvé :")

            for cle, valeur in ds.items():
                print(f"{cle} : {valeur}")

            trouve = True

    if not trouve:
        print("Dataset introuvable.")





def modifier():

    nom = input("Nom du dataset à modifier : ").lower()

    for ds in datasets:

        if ds["nom"].lower() == nom:

            print("Nouvelles informations")

            ds["nom"] = input("Nom : ")
            ds["lignes"] = int(input("Nombre de lignes : "))
            ds["colonnes"] = int(input("Nombre de colonnes : "))
            ds["taille"] = float(input("Taille : "))

            print("Modification effectuée.")
            return

    print("Dataset introuvable.")



def supprimer():

    nom = input("Nom du dataset à supprimer : ").lower()

    for ds in datasets:

        if ds["nom"].lower() == nom:

            datasets.remove(ds)
            print("Dataset supprimé.")
            return

    print("Dataset introuvable.")



def trier():

    datasets.sort(key=lambda d: d["nom"].lower())

    print("Datasets triés par nom.")


def statistiques():

    print("\n===== STATISTIQUES =====")

    if len(datasets) == 0:
        print("Aucun dataset.")
        return

    nb = len(datasets)

    total_lignes = sum(ds["lignes"] for ds in datasets)

    moyenne_colonnes = sum(ds["colonnes"] for ds in datasets) / nb

    publics = sum(1 for ds in datasets if ds["public"])

    prives = nb - publics

    csv = sum(1 for ds in datasets if ds["format"] == "CSV")

    json = sum(1 for ds in datasets if ds["format"] == "JSON")

    repartition = {
        domaine: sum(1 for ds in datasets if ds["domaine"] == domaine)
        for domaine in DOMAINES
    }

    print("Nombre de datasets :", nb)
    print("Nombre total de lignes :", total_lignes)
    print("Nombre moyen de colonnes :", round(moyenne_colonnes, 2))
    print("Datasets publics :", publics)
    print("Datasets privés :", prives)
    print("Nombre de datasets CSV :", csv)
    print("Nombre de datasets JSON :", json)

    print("\nRépartition par domaine")

    for domaine, nombre in repartition.items():
        print(f"{domaine} : {nombre}")


def sauvegarder():

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

        writer.writerows(datasets)

    print("Sauvegarde effectuée.")


def recharger():

    global datasets

    datasets = []

#Gestion  des exceptions pour que le programme continue de fonctionner.
    try:

      with open("datasets.csv", "r", encoding="utf-8") as fichier:

        lecteur = list(csv.DictReader(fichier))

        if len(lecteur) == 0:
            raise EOFError

    except EOFError:

     print("Le fichier est vide.")

    with open("datasets.csv", "r", encoding="utf-8") as fichier:

        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:

            ligne["lignes"] = int(ligne["lignes"])
            ligne["colonnes"] = int(ligne["colonnes"])
            ligne["taille"] = float(ligne["taille"])
            ligne["public"] = ligne["public"] == "True"

            datasets.append(ligne)
#Gestion  des exceptions pour que le programme continue de fonctionner.
        try:

           recharger()

        except FileNotFoundError:

         print("Le fichier datasets.csv n'existe pas.")

    print("Chargement terminé.")

# Menu

while True:

    print("""
===========================
1. Ajouter un dataset
2. Afficher les datasets
3. Rechercher
4. Modifier
5. Supprimer
6. Trier
7. Statistiques
8. Quitter
===========================
""")

    choix = input("Votre choix : ")

    if choix == "1":
        ajouter_dataset()
        input("Appuyez sur Entrée pour continuer...")
    elif choix == "2":
        afficher()
        input("Appuyez sur Entrée pour continuer...")
    elif choix == "3":
        rechercher()
        input("Appuyez sur Entrée pour continuer...")
    elif choix == "4":
        modifier()
        input("Appuyez sur Entrée pour continuer...")
    elif choix == "5":
        supprimer()
        input("Appuyez sur Entrée pour continuer...")
    elif choix == "6":
        trier()
        input("Appuyez sur Entrée pour continuer...")
    elif choix == "7":
        statistiques()
        input("Appuyez sur Entrée pour continuer...")

    elif choix == "8":
        print("Fin du programme.")
        break

    else:
        print("Choix invalide.")
        input("Appuyez sur Entrée pour refaire un choix ...")
