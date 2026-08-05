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