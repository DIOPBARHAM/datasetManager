import csv
import os
from datasets.gestion import datasets
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


