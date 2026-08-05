# 3- Demandez à l utilisateur de saisir les métadonnées d un dataset

nom = input("Nom du dataset : ")
domaine = input("Domaine : ")
lignes = int(input("Nombre de lignes : "))
colonnes = int(input("Nombre de colonnes : "))
taille = float(input("Taille en Mo : "))
format_dataset = input("Format (csv ou json) : ")
public = input("Dataset public (true ou false) : ")
# 4-Affichez ensuite un résumé formaté.
print("\n===== Résumé du dataset =====")
print("Nom :", nom)
print("Domaine :", domaine)
print("Nombre de lignes :", lignes)
print("Nombre de colonnes :", colonnes)
print("Taille :", taille, "Mo")
print("Format :", format_dataset)
print("Public :", public)

# Créez un menu interactif (provisoire)

choix = ""

while choix != "4":

    print("\n========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher")
    print("4. Quitter")
    print("========================")

    choix = input("Votre choix : ")

    if choix == "1":
        print("Ajout d'un dataset")

    elif choix == "2":
        print("Affichage des datasets")

    elif choix == "3":
        print("Recherche d'un dataset")

    elif choix == "4":
        print("Fermeture du programme")

    else:
        print("Choix invalide")

# 6-Créez un dictionnaire pour stocker les métadonnées de chaque dataset

dataset = {
    "nom": nom,
    "domaine": domaine,
    "lignes": lignes,
    "colonnes": colonnes,
    "taille": taille,
    "format": format_dataset,
    "public": public
}

print("\n===== Résumé du dataset =====")

print(dataset)

# 7- Créez un tuple contenant les domaines autorisés.

domaines_autorises = (
    "Santé",
    "Finance",
    "Agriculture",
    "Transport",
    "Education"
)

# 8- Vérifiez que le domaine saisi, à la question 3, appartient au tuple

if domaine in domaines_autorises:
    print("Domaine valide")
else:
    print("Domaine non autorisé")

# 9- Créez une liste contenant les datasets. Chaque ajout est enregistré dans la liste

datasets = []

datasets.append(dataset)

print("\nListe des datasets :")
print(datasets)


# Fonction Ajouter un dataset

def ajouter_dataset():

    print("\n=== Nouveau Dataset ===")

    nom = input("Nom : ")
    while True:
        domaine = input("Domaine : ").title()

        if domaine in domaines_autorises:
            break
        else:
            print("Domaine invalide.")
            print("Domaines autorisés :", domaines_autorises)


    lignes = int(input("Nombre de lignes : ")) 
    colonnes = int(input("Nombre de colonnes : "))    
    taille = float(input("Taille (Mo) : "))
    format_ds = input("Format (CSV/JSON) : ").upper()
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


# Fonction afficher
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

# Fonction rechercher

def rechercher():

    nom = input("Nom du dataset : ").lower()

    trouve = False
    for ds in datasets:

     if ds["nom"].lower() == nom.lower():

        print(ds)
        return

    for ds in datasets:

        if ds["nom"].lower() == nom:
            print("\nDataset trouvé :")

            for cle, valeur in ds.items():
                print(f"{cle} : {valeur}")

            trouve = True

    if not trouve:
        print("Dataset introuvable.")


# Fonction Modifier

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

# fonction Supprimer
def supprimer():

    nom = input("Nom du dataset à supprimer : ").lower()

    for ds in datasets:

        if ds["nom"].lower() == nom:

            datasets.remove(ds)
            print("Dataset supprimé.")
            return

    print("Dataset introuvable.")


# Fonction Trier
def trier():

    datasets.sort(key=lambda d: d["nom"].lower())

    print("Datasets triés par nom.")



# 11-Afficher les Statistiques
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
        for domaine in domaines_autorises
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

statistiques()