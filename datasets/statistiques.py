import csv
import os

datasets = []

DOMAINES = (
    "Santé",
    "Finance",
    "Agriculture",
    "Transport",
    "Education"
)

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