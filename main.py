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