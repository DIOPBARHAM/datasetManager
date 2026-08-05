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





def modifier_datasets():

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
    else:
        datasets.sort(key=lambda d: d["nom"].lower())
        print("Datasets triés par nom.")
