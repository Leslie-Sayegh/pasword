#créer stocker fichier MdP 
import json

utilisateur = '{"name" : "Leslie",\
    "email" : "leslie.sayegh@laplateforme.io",\
        "MdP" : "Siriana06"}'
#recu données forme dico
personneDict = json.loads (utilisateur)
print (personneDict)

with open("/chemin/vers/fichier.json", "r") as f:
    data = json.load(f)

def password_check(passwd) :
    
    maj = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    caracterrspecial = ['!', '@', '#', '$', '%', '^', '&', '*']
    val= True

id = input("Identifiant : ")

mdp = input("Mot de passe : ")
mdp1 = "b"

if len(mdp) >= 8 :
    if True in (car in "maj" for car in mdp) :
        if (car in "chiffres" for car in mdp) :
            if (car in "caracterrspecial" for car in mdp) :
                if(mdp1 == ("b")):
                 print ("Bienvenue !!")

else :                  
    print ("Invalid Password !!")
     
    if input("réentrez le mot de passe pour vérifier: ") == mdp:
         confirm = True

 
import hashlib
 
# La chaîne de caractères à hasher
string_to_hash = "example_string"
 
# Création d'un objet hash SHA-256
hash_object = hashlib.sha256()
 
# Mise à jour de l'objet hash avec la chaîne de caractères à hasher
hash_object.update(string_to_hash.encode())
 
# Récupération du hash en hexadécimal
hex_hash = hash_object.hexdigest()
 
print(f"Hash de la chaîne '{string_to_hash}' : {hex_hash}")

if id == "a" and mdp == "b":
    print("Bienvenue")
elif id == "a" and mdp != "b":
    print("Mot de passe incorrect...")
elif id != "a" and mdp == "b":
    print("Identifiant incorrect...")

import json
with open("/chemin/vers/fichier.json", "r") as f:
    data = json.load(f)